from __future__ import annotations

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field
from crewai.flow.flow import Flow, listen, start, router

from app.dataset_loader import DatasetManager
from app.gemma_client import GemmaClient
from app.source_registry import TRUSTED_SOURCES


# ── Constants ─────────────────────────────────────────────────────────────────

EMERGENCY_FLAGS = [
    "heavy bleeding", "soaking pad", "severe headache", "blurred vision",
    "chest pain", "difficulty breathing", "seizure", "high fever",
    "fainting", "suicidal", "want to harm", "hurt my baby", "harm my baby",
]

CRISIS_KEYWORDS = [
    "suicidal", "want to die", "end my life", "harm myself",
    "hurt my baby", "want to harm", "can't go on",
]

CHATBOT_SYSTEM_PROMPT = """
You are Ira, a warm, empathetic, and trustworthy companion for postpartum mothers.
You listen with patience and respond with kindness.
You can talk about health, baby care, emotional wellbeing, home and family matters.
Never dismiss her feelings. Never prescribe medications or diagnose.
If she mentions emergency symptoms, gently urge her to seek immediate help.
If she expresses suicidal thoughts, respond with warmth and strongly encourage
her to call a trusted person or doctor immediately.
Keep responses warm and conversational, not clinical.
Respond in the same language the mother writes in.
"""

TRACKER_STORE = Path("/kaggle/working/data/health_tracker.json")
TRACKER_STORE.parent.mkdir(parents=True, exist_ok=True)

COMMUNITY_STORE = Path("/kaggle/working/data/community.json")
COMMUNITY_STORE.parent.mkdir(parents=True, exist_ok=True)


# ── Tracker helpers ───────────────────────────────────────────────────────────

def _load_tracker() -> list:
    if not TRACKER_STORE.exists():
        return []
    try:
        with open(TRACKER_STORE) as f:
            return json.load(f)
    except Exception:
        return []


def _save_tracker(data: list):
    with open(TRACKER_STORE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _validate_health_value(key: str, value: float) -> tuple[bool, str]:
    """Validate health readings to prevent unsafe values."""
    validation_rules = {
        "bp_systolic":        (50, 250, "Blood pressure systolic must be between 50-250 mmHg"),
        "bp_diastolic":       (30, 180, "Blood pressure diastolic must be between 30-180 mmHg"),
        "sugar_normal":       (20, 600, "Blood sugar must be between 20-600 mg/dL"),
        "sugar_fasting":      (20, 600, "Fasting sugar must be between 20-600 mg/dL"),
        "sugar_postprandial": (20, 600, "Postprandial sugar must be between 20-600 mg/dL"),
        "temperature":        (32.0, 45.0, "Temperature must be between 32-45°C"),
        "heart_rate":         (30, 250, "Heart rate must be between 30-250 bpm"),
        "blood_oxygen":       (50, 100, "Blood oxygen must be between 50-100%"),
        "thyroid_tsh":        (0.001, 100.0, "TSH must be between 0.001-100 mIU/L"),
        "weight":             (20.0, 300.0, "Weight must be between 20-300 kg"),
        "sleep_hours":        (0.0, 24.0, "Sleep hours must be between 0-24 hours"),
        "hydration_glasses":  (0, 50, "Hydration must be between 0-50 glasses"),
    }

    if key in validation_rules:
        min_val, max_val, error_msg = validation_rules[key]
        if not (min_val <= value <= max_val):
            return False, error_msg

    return True, ""


def _flag_alerts(entry: dict) -> list:
    alerts = []
    if entry.get("bp_systolic"):
        if entry["bp_systolic"] > 140:
            alerts.append("⚠️ High blood pressure — systolic > 140 mmHg")
        if entry["bp_systolic"] < 90:
            alerts.append("⚠️ Low blood pressure — systolic < 90 mmHg")
    if entry.get("bp_diastolic") and entry["bp_diastolic"] > 90:
        alerts.append("⚠️ High blood pressure — diastolic > 90 mmHg")
    if entry.get("sugar_normal") and not (70 <= entry["sugar_normal"] <= 140):
        alerts.append("⚠️ Blood sugar (normal) out of range (70–140 mg/dL)")
    if entry.get("sugar_fasting") and not (70 <= entry["sugar_fasting"] <= 100):
        alerts.append("⚠️ Fasting sugar out of range (70–100 mg/dL)")
    if entry.get("sugar_postprandial") and entry["sugar_postprandial"] > 140:
        alerts.append("⚠️ Postprandial sugar high (> 140 mg/dL)")
    if entry.get("temperature") and entry["temperature"] > 38.0:
        alerts.append("⚠️ Fever detected — temperature > 38°C")
    if entry.get("heart_rate"):
        if entry["heart_rate"] > 100:
            alerts.append("⚠️ High heart rate — > 100 bpm")
        if entry["heart_rate"] < 50:
            alerts.append("⚠️ Low heart rate — < 50 bpm")
    if entry.get("blood_oxygen") and entry["blood_oxygen"] < 95:
        alerts.append("⚠️ Low blood oxygen — SpO2 < 95%")
    if entry.get("sleep_hours") and entry["sleep_hours"] < 4:
        alerts.append("⚠️ Very low sleep — less than 4 hours")
    if entry.get("thyroid_tsh") and not (0.4 <= entry["thyroid_tsh"] <= 4.0):
        alerts.append("⚠️ TSH out of normal range (0.4–4.0 mIU/L)")
    if entry.get("hydration_glasses") and entry["hydration_glasses"] < 6:
        alerts.append("⚠️ Low hydration — less than 6 glasses")
    return alerts


# ── Community helpers ─────────────────────────────────────────────────────────

def _load_community() -> list:
    if not COMMUNITY_STORE.exists():
        return []
    try:
        with open(COMMUNITY_STORE) as f:
            return json.load(f)
    except Exception:
        return []


def _save_community(data: list):
    with open(COMMUNITY_STORE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ── Flow State ────────────────────────────────────────────────────────────────

class PostpartumState(BaseModel):
    id:              str       = Field(default_factory=lambda: str(uuid.uuid4()))
    symptoms:        List[str] = Field(default_factory=list)
    days_postpartum: int       = 0
    language:        str       = "English"
    phase:           str       = "early_postpartum"
    journal_text:    str       = ""
    audio_path:      str       = ""
    safety_result:   str       = ""
    context:         str       = ""
    health_result:   str       = ""
    triage_result:   str       = ""
    diet_result:     str       = ""
    journal_result:  str       = ""
    audio_result:    str       = ""
    is_emergency:    bool      = False


# ── Flow ──────────────────────────────────────────────────────────────────────

class PostpartumFlow(Flow[PostpartumState]):
    initial_state = PostpartumState

    def __init__(self, dm: DatasetManager, gc: GemmaClient):
        super().__init__()
        self.dm = dm
        self.gc = gc

    # ── 1. Safety ─────────────────────────────────────────────────────────────

    @start()
    def run_safety(self):
        text    = ", ".join(self.state.symptoms).lower()
        matches = [f for f in EMERGENCY_FLAGS if f in text]
        if matches:
            self.state.safety_result = (
                "🚨 EMERGENCY ALERT 🚨\n"
                f"Warning signs detected: {', '.join(matches)}\n"
                "Please go to the nearest hospital immediately."
            )
        else:
            self.state.safety_result = "SAFE"

    @router(run_safety)
    def route_safety(self):
        if "EMERGENCY" in self.state.safety_result:
            self.state.is_emergency = True
            return "emergency"
        return "continue"

    @listen("emergency")
    def handle_emergency(self):
        pass

    # ── 2. Retrieval ──────────────────────────────────────────────────────────

    @listen("continue")
    def run_retrieval(self):
        query = ", ".join(self.state.symptoms) or self.state.journal_text
        self.state.context = self.dm.get_context(query)

    # ── 3. Health ─────────────────────────────────────────────────────────────

    @listen(run_retrieval)
    def run_health(self):
        enable_thinking = self.state.audio_path == "THINKING_MODE"  # Hack to pass thinking flag

        if enable_thinking:
            result = self.gc.generate_with_thinking(
                system_prompt="You are Ira, a warm postpartum health assistant.",
                user_prompt=f"""
Symptoms: {', '.join(self.state.symptoms)}
Days postpartum: {self.state.days_postpartum}
Context: {self.state.context}
Identify possible postpartum conditions in simple comforting language.
Do NOT suggest medications. Respond in {self.state.language}.
""",
                max_new_tokens=256,
            )
            self.state.health_result = result["answer"]
            self.state.audio_result = result["thinking"]  # Store thinking in audio_result
        else:
            self.state.health_result = self.gc.generate(
                system_prompt="You are Ira, a warm postpartum health assistant.",
                user_prompt=f"""
Symptoms: {', '.join(self.state.symptoms)}
Days postpartum: {self.state.days_postpartum}
Context: {self.state.context}
Identify possible postpartum conditions in simple comforting language.
Do NOT suggest medications. Respond in {self.state.language}.
""",
                max_new_tokens=256,
            )

    # ── 4. Triage ─────────────────────────────────────────────────────────────

    @listen(run_health)
    def run_triage(self):
        self.state.triage_result = self.gc.generate(
            system_prompt="You are a postpartum medical triage specialist.",
            user_prompt=f"""
Days postpartum: {self.state.days_postpartum}
Symptoms: {', '.join(self.state.symptoms)}
Health analysis: {self.state.health_result}
Classify urgency as: EMERGENCY, HIGH RISK, URGENT, MONITOR, or SELF CARE.
Format:
URGENCY: <level>
EXPLANATION: <one sentence>
GUIDANCE:
1. <step>
2. <step>
3. <step>
Respond in {self.state.language}. Do NOT suggest medications.
""",
            max_new_tokens=256,
        )

    # ── 5. Diet ───────────────────────────────────────────────────────────────

    @listen(run_health)
    def run_diet(self):
        guidelines = self.dm.get_diet_data(self.state.phase)
        self.state.diet_result = self.gc.generate(
            system_prompt="You are Ira, a warm postpartum nutrition expert.",
            user_prompt=f"""
Phase: {self.state.phase.replace('_', ' ').title()}
Symptoms: {', '.join(self.state.symptoms)}
Guidelines: {chr(10).join(f'- {g}' for g in guidelines)}
Provide recommended foods, drinks, foods to avoid, hydration tips.
Respond in {self.state.language}.
""",
            max_new_tokens=256,
        )

    # ── 6. Journal ────────────────────────────────────────────────────────────

    @listen(run_health)
    def run_journal(self):
        if not self.state.journal_text.strip():
            return
        context = self.dm.get_context(self.state.journal_text)
        self.state.journal_result = self.gc.generate(
            system_prompt="You are Ira, a compassionate postpartum emotional support assistant.",
            user_prompt=f"""
Journal entry: {self.state.journal_text}
Context: {context}
Respond in {self.state.language} with:
1. Emotional state (one or two words)
2. Stress level (Low / Moderate / High)
3. PPD signals (list any, or 'None detected')
4. A gentle supportive message
Do NOT diagnose. Do NOT suggest medications.
""",
            max_new_tokens=256,
        )


    # ── Tracker (called directly, not part of flow) ───────────────────────────

    def run_tracker(self, entry: dict) -> dict:
        # Validate all numeric health values before saving
        validation_errors = []
        for key, value in entry.items():
            if value is not None and isinstance(value, (int, float)) and key not in ["id", "timestamp", "date"]:
                is_valid, error_msg = _validate_health_value(key, value)
                if not is_valid:
                    validation_errors.append(error_msg)

        if validation_errors:
            return {
                "entry": None,
                "alerts": [],
                "errors": validation_errors,
                "summary": None
            }

        entry["id"]        = str(uuid.uuid4())
        entry["timestamp"] = datetime.now().strftime("%d %b %Y, %I:%M %p")
        entry["date"]      = datetime.now().strftime("%d %b %Y")
        entries = _load_tracker()
        entries.append(entry)
        _save_tracker(entries)
        alerts = _flag_alerts(entry)

        # Generate AI summary if there are alerts
        summary = None
        if alerts:
            try:
                summary = self.analyze_tracker_entry(entry, self.state.language)
            except Exception:
                summary = None

        return {
            "entry": entry,
            "alerts": alerts,
            "errors": [],
            "summary": summary
        }

    def analyze_tracker_entry(self, entry: dict, language: str) -> str:
        readable = {
            k: v for k, v in entry.items()
            if v is not None and k not in ["id", "timestamp", "date"]
        }
        alerts = _flag_alerts(entry)
        return self.gc.generate(
            system_prompt="You are Ira, a warm postpartum health assistant.",
            user_prompt=f"""
A postpartum mother logged these health readings:
{json.dumps(readable, indent=2)}

{"Alerts: " + ", ".join(alerts) if alerts else "All readings appear normal."}

Give a warm 3-4 sentence summary of what these readings mean for her health
and gently advise next steps. Respond in {language}.
""",
            max_new_tokens=200,
        )

    def get_tracker_history(self) -> list:
        return _load_tracker()

    # ── Chat (called directly, not part of flow) ──────────────────────────────

    def chat(self, user_message: str, history: list, language: str = "English", user_context: dict = None) -> str:
        if not user_message.strip():
            return ""
        if any(kw in user_message.lower() for kw in CRISIS_KEYWORDS):
            return (
                "I hear you, and I'm really glad you shared this with me. 💙\n\n"
                "What you're feeling matters deeply. Please reach out to someone "
                "you trust right now — a family member, your doctor, or a helpline. "
                "You are not alone, and you deserve support and care.\n\n"
                "I'm here with you. Please talk to someone who can help you in person."
            )

        # Build context-aware system prompt
        context_prompt = CHATBOT_SYSTEM_PROMPT
        if user_context:
            context_prompt += f"\n\nContext about the mother:\n"
            context_prompt += f"- Name: {user_context.get('name', 'unknown')}\n"
            context_prompt += f"- Days postpartum: {user_context.get('postpartum_days', 'unknown')}\n"
            context_prompt += f"- Number of children: {user_context.get('num_children', 'unknown')}\n"
            context_prompt += f"- Status: {user_context.get('working_status', 'unknown')}\n"
            if user_context.get('feeding_method') and user_context['feeding_method'] != "Prefer not to say":
                context_prompt += f"- Feeding method: {user_context['feeding_method']}\n"
            context_prompt += "\nUse this context to provide personalized, relevant support."

        history_text = ""
        for turn in history[-5:]:
            history_text += f"Mother: {turn['user']}\nIra: {turn['ira']}\n\n"

        return self.gc.generate(
            system_prompt=context_prompt,
            user_prompt=(
                f"{history_text}"
                f"Mother: {user_message}\n"
                f"Respond in {language}. Be warm and concise."
            ),
            max_new_tokens=300,
        )

    # ── Community (called directly) ───────────────────────────────────────────

    def post_tip(self, author: str, text: str, language: str) -> dict:
        tips = _load_community()
        tip = {
            "id":        str(uuid.uuid4()),
            "author":    author or "Anonymous",
            "language":  language,
            "text":      text,
            "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "replies":   [],
            "likes":     0,
        }
        tips.insert(0, tip)
        _save_community(tips)
        return tip

    def post_reply(self, tip_id: str, author: str, text: str) -> bool:
        tips = _load_community()
        for tip in tips:
            if tip["id"] == tip_id:
                tip["replies"].append({
                    "id":        str(uuid.uuid4()),
                    "author":    author or "Anonymous",
                    "text":      text,
                    "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                })
                _save_community(tips)
                return True
        return False

    def like_tip(self, tip_id: str) -> bool:
        tips = _load_community()
        for tip in tips:
            if tip["id"] == tip_id:
                tip["likes"] += 1
                _save_community(tips)
                return True
        return False

    def get_tips(self) -> list:
        return _load_community()