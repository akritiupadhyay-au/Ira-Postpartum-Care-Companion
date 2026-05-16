"""Streamlit UI for Postpartum Care Companion — CrewAI Flow version."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path("/kaggle/working/Ira-Postpartum-Care-Companion")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from streamlit_mic_recorder import mic_recorder
import tempfile
from pathlib import Path

# Configure Streamlit for Kaggle offline mode
st.set_page_config(
    page_title="Postpartum Care Companion",
    page_icon="🤱",
    layout="wide",
    initial_sidebar_state="expanded",
)

from app.crewai_flow import PostpartumFlow
from app.translations import t

PHASE_KEY_MAP = {
    "Immediate (0–7 days)":  "immediate_postpartum",
    "Early (8–42 days)":     "early_postpartum",
    "Late (43+ days)":       "late_postpartum",
}


# ── Audio Helper Functions ────────────────────────────────────────────────────

def transcribe_audio_with_gemma(gemma_client, audio_path: str, language: str = "English") -> str:
    """Transcribe audio using Gemma's audio capability."""
    try:
        system_prompt = f"""You are a medical transcription assistant.
Transcribe the audio accurately. The speaker is a postpartum mother describing symptoms, feelings, or questions.
Transcribe in {language}. If the audio is unclear, do your best to capture the meaning."""

        prompt = "Transcribe this audio message from a new mother. Provide only the transcription, no additional commentary."

        transcription = gemma_client.generate_with_audio(
            audio_path=audio_path,
            prompt=prompt,
            system_prompt=system_prompt,
            max_new_tokens=512
        )
        return transcription.strip()
    except Exception as e:
        return f"[Audio transcription error: {str(e)}]"


# ── Init (cached) ─────────────────────────────────────────────────────────────

@st.cache_resource
def get_clients():
    from app.gemma_client import GemmaClient
    from app.dataset_loader import DatasetManager
    return GemmaClient(), DatasetManager()


gemma_client, dataset_manager = get_clients()


# ── Session state ─────────────────────────────────────────────────────────────

st.session_state.setdefault("language", "English")
st.session_state.setdefault("page", "Wellness Check")
st.session_state.setdefault("user_profile", None)
st.session_state.setdefault("disclaimer_accepted", False)


# ── Welcome Page ──────────────────────────────────────────────────────────────

if st.session_state.user_profile is None:
    lang = st.session_state.language
    st.title(t("welcome_title", lang))
    st.markdown(
        f"### {t('welcome_subtitle', lang)}\n\n"
        f"{t('welcome_intro', lang)}"
    )

    st.divider()

    with st.form("user_profile_form"):
        st.markdown(f"#### {t('tell_us', lang)}")

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input(
                t("your_name", lang),
                placeholder=t("placeholder_name", lang),
                help="We'll use this to personalize your experience"
            )

            age = st.number_input(
                t("your_age", lang),
                min_value=15,
                max_value=60,
                value=28,
                help="This helps us provide age-appropriate guidance"
            )

            postpartum_days = st.number_input(
                t("days_since_delivery", lang),
                min_value=0,
                max_value=730,
                value=7,
                help="How many days has it been since you gave birth?"
            )

        with col2:
            num_children = st.number_input(
                t("number_of_children", lang),
                min_value=1,
                max_value=10,
                value=1,
                help="Including your most recent baby"
            )

            working_status = st.selectbox(
                t("current_status", lang),
                [
                    "Stay-at-home mother",
                    "Working mother (on leave)",
                    "Working mother (returned to work)",
                    "Student",
                    "Looking for work",
                    "Other"
                ]
            )

            preferred_lang = st.selectbox(
                t("preferred_language", lang),
                ["English", "Hindi", "Hinglish", "Tamil", "Telugu", "Bengali",
                 "Marathi", "Gujarati", "Kannada", "Malayalam", "Odia",
                 "Punjabi", "Urdu", "Nepali", "Assamese"]
            )

        st.markdown(f"##### {t('optional_info', lang)}")

        delivery_type = st.selectbox(
            t("delivery_type", lang),
            ["Prefer not to say", "Normal vaginal delivery", "C-section", "Assisted delivery (forceps/vacuum)"]
        )

        feeding_method = st.selectbox(
            t("feeding_method", lang),
            ["Prefer not to say", "Breastfeeding", "Formula feeding", "Mixed feeding"]
        )

        st.divider()

        # Disclaimer as part of the form
        st.warning(
            f"**{t('disclaimer_title', lang)}**\n\n"
            f"{t('disclaimer_text', lang)}"
        )

        agree_disclaimer = st.checkbox(
            t("disclaimer_accept", lang),
            value=False
        )

        submitted = st.form_submit_button(t("continue_to_app", lang), type="primary", use_container_width=True)

        if submitted:
            if not name.strip():
                st.error("Please enter your name")
            elif not agree_disclaimer:
                st.error("Please accept the medical disclaimer to continue")
            else:
                # Determine postpartum phase
                if postpartum_days <= 7:
                    phase = "immediate_postpartum"
                elif postpartum_days <= 42:
                    phase = "early_postpartum"
                else:
                    phase = "late_postpartum"

                # Save profile
                st.session_state.user_profile = {
                    "name": name.strip(),
                    "age": age,
                    "postpartum_days": postpartum_days,
                    "num_children": num_children,
                    "working_status": working_status,
                    "delivery_type": delivery_type,
                    "feeding_method": feeding_method,
                    "phase": phase,
                }
                st.session_state.language = preferred_lang
                st.session_state.disclaimer_accepted = True
                st.success(f"Welcome, {name}! Redirecting to your personalized dashboard...")
                st.rerun()

    st.stop()


# ── Medical Disclaimer (legacy, now in welcome page) ─────────────────────────

if "disclaimer_accepted" not in st.session_state:
    st.session_state.disclaimer_accepted = False

if not st.session_state.disclaimer_accepted:
    st.title("🤱 Postpartum Care Companion")
    st.warning(
        "### ⚕️ Medical Disclaimer\n\n"
        "This application provides **educational information only** and is **not a substitute "
        "for professional medical advice, diagnosis, or treatment**.\n\n"
        "**Important:**\n"
        "- Always consult your healthcare provider for medical concerns\n"
        "- In case of emergency, call your local emergency number immediately\n"
        "- This app does not replace visits to your doctor\n"
        "- AI-generated advice may not be accurate for your specific situation\n\n"
        "By using this app, you acknowledge that you understand these limitations."
    )
    if st.button("I Understand and Accept", type="primary"):
        st.session_state.disclaimer_accepted = True
        st.rerun()
    st.stop()

# ── Header ────────────────────────────────────────────────────────────────────

lang = st.session_state.language
user_name = st.session_state.user_profile.get("name", "")
st.title(f"{t('welcome_back', lang)}, {user_name}!")
st.caption(t("tagline", lang))


# ── Sidebar ───────────────────────────────────────────────────────────────────

# User Profile Summary
lang = st.session_state.language
profile = st.session_state.user_profile
st.sidebar.markdown(f"### 👤 {profile['name']}")

# Calculate phase label
if profile['postpartum_days'] <= 7:
    phase_label = "Immediate Recovery"
    phase_emoji = "🌱"
elif profile['postpartum_days'] <= 42:
    phase_label = "Early Recovery"
    phase_emoji = "🌿"
else:
    phase_label = "Late Recovery"
    phase_emoji = "🌳"

st.sidebar.markdown(f"{phase_emoji} **{phase_label}** (Day {profile['postpartum_days']})")
st.sidebar.caption(f"👶 {profile['num_children']} child{'ren' if profile['num_children'] > 1 else ''} • 🎂 Age {profile['age']}")

if st.sidebar.button(t("update_profile", lang), use_container_width=True):
    st.session_state.user_profile = None
    st.rerun()

st.sidebar.divider()

# Navigation
lang = st.session_state.language
st.sidebar.title("Navigation")

# Create navigation options with translations
nav_options = [
    ("Wellness Check", t("nav_wellness", lang)),
    ("📸 Visual Health Check", t("nav_visual", lang)),
    ("🎥 Video Health Check", t("nav_video", lang)),
    ("Nutrition", t("nav_nutrition", lang)),
    ("Track Your Health", t("nav_tracker", lang)),
    ("Share with Ira", t("nav_chat", lang)),
    ("My Journal", t("nav_journal", lang)),
    ("🔍 Health Insights", t("nav_insights", lang)),
    ("Mom's Circle", t("nav_community", lang)),
    ("Articles", t("nav_articles", lang))
]

# Display translated labels but store English keys
page_display = st.sidebar.radio("Go to", [label for _, label in nav_options])

# Map back to English key for page routing
page_map = {label: key for key, label in nav_options}
page = page_map.get(page_display, "Wellness Check")
st.session_state.page = page

st.sidebar.divider()

# Language selector
current_lang = st.session_state.language
lang_index = ["English", "Hindi", "Hinglish", "Tamil", "Telugu", "Bengali", "Marathi", "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi","Urdu", "Nepali", "Assamese"].index(current_lang) if current_lang in ["English", "Hindi", "Hinglish", "Tamil", "Telugu", "Bengali", "Marathi", "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi","Urdu", "Nepali", "Assamese"] else 0

lang_new = st.sidebar.selectbox(
    t("language", current_lang),
    ["English", "Hindi", "Hinglish", "Tamil", "Telugu", "Bengali", "Marathi", "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi","Urdu", "Nepali", "Assamese"],
    index=lang_index,
    key="language_selector"
)
if lang_new != st.session_state.language:
    st.session_state.language = lang_new
    st.rerun()
st.sidebar.markdown(f"🌐 **{st.session_state.language}**")

st.sidebar.divider()
st.sidebar.caption("⚕️ This app does not replace medical advice. Always consult your healthcare provider.")


# ── Triage ────────────────────────────────────────────────────────────────────

if page == "📸 Visual Health Check":
    from app.streamlit_image_check import render_image_check_page
    render_image_check_page(gemma_client, st.session_state.user_profile)

elif page == "🎥 Video Health Check":
    from app.streamlit_video_check import render_video_check_page
    render_video_check_page(gemma_client, st.session_state.user_profile)

elif page == "Wellness Check":
    lang = st.session_state.language
    st.subheader(t("symptom_checker", lang))

    profile = st.session_state.user_profile
    st.info(t("hi_message", lang).format(name=profile['name'], days=profile['postpartum_days']))

    days = st.number_input(t("days_postpartum", lang), min_value=0, max_value=365, value=profile['postpartum_days'])
    symptoms = st.text_area(t("symptoms", lang), placeholder=t("placeholder_symptoms", lang))

    # Audio input option
    st.markdown("---")
    st.markdown("**🎤 Or record your symptoms with voice**")
    audio_bytes = mic_recorder(
        start_prompt="🎙️ Start Recording",
        stop_prompt="⏹️ Stop Recording",
        just_once=False,
        use_container_width=False,
        key="wellness_audio"
    )

    if audio_bytes:
        # Save audio and transcribe
        temp_dir = Path(tempfile.gettempdir()) / "ira_audio"
        temp_dir.mkdir(exist_ok=True)
        audio_path = temp_dir / f"wellness_{profile['name']}.wav"

        with open(audio_path, "wb") as f:
            f.write(audio_bytes['bytes'])

        st.audio(audio_bytes['bytes'], format='audio/wav')

        with st.spinner("🎧 Transcribing your voice message..."):
            transcription = transcribe_audio_with_gemma(gemma_client, str(audio_path), lang)

        if transcription and not transcription.startswith("[Audio transcription error"):
            st.success("✅ Audio transcribed!")
            st.info(f"**Transcription:** {transcription}")
            # Append to symptoms
            if symptoms:
                symptoms = f"{symptoms}\n\n[Voice message]: {transcription}"
            else:
                symptoms = transcription

    # Thinking mode toggle
    col1, col2 = st.columns([3, 1])
    with col2:
        show_thinking = st.checkbox(t("show_ai_reasoning", lang), value=False, help=t("show_ai_reasoning_help", lang))

    if st.button(t("get_guidance", lang), type="primary"):
        symptom_list = [s.strip() for s in symptoms.split(",") if s.strip()]

        if not symptom_list and symptoms.strip():
            symptom_list = [symptoms.strip()]

        if not symptom_list:
            st.warning(t("please_describe_symptoms", lang))
            st.stop()

        try:
            with st.spinner(t("analyzing", lang)):
                flow = PostpartumFlow(dm=dataset_manager, gc=gemma_client)
                flow.kickoff(inputs={
                    "symptoms":        symptom_list,
                    "days_postpartum": int(days),
                    "language":        st.session_state.language,
                    "phase":           profile['phase'],
                    "journal_text":    "",
                    "audio_path":      "THINKING_MODE" if show_thinking else "",
                })
            state = flow.state

            if state.is_emergency:
                st.error(state.safety_result)
                st.stop()

            # Show thinking process if enabled
            if show_thinking and state.audio_result:
                st.markdown(t("how_ira_analyzed", lang))
                with st.expander(t("view_ai_reasoning", lang), expanded=True):
                    st.info(state.audio_result)
                st.markdown("---")

            st.markdown(t("triage_guidance", lang))
            if state.triage_result:
                st.write(state.triage_result)
            else:
                st.warning(t("could_not_generate_guidance", lang))

            if state.diet_result:
                with st.expander(t("diet_recommendations", lang)):
                    st.write(state.diet_result)

            with st.expander(t("pipeline_trace", lang)):
                st.write(f"• Language: {st.session_state.language}")
                st.write(f"• Safety: {state.safety_result}")
                st.write(f"• Context: {'Yes' if state.context else 'No'}")
                st.write(f"• Health: {'Done' if state.health_result else 'Skipped'}")
                st.write(f"• Triage: {'Done' if state.triage_result else 'Skipped'}")
                st.write(f"• Thinking mode: {'Enabled' if show_thinking else 'Disabled'}")

        except Exception as e:
            st.error(f"❌ An error occurred during analysis: {str(e)}")
            st.warning("Please try again. If the problem persists, consult your healthcare provider directly.")
            st.stop()
# ── Diet ──────────────────────────────────────────────────────────────────────

elif page == "Nutrition":
    lang = st.session_state.language
    st.subheader(t("diet_suggestions", lang))

    profile = st.session_state.user_profile

    # Auto-select current phase
    current_phase_label = {
        "immediate_postpartum": "Immediate (0–7 days)",
        "early_postpartum": "Early (8–42 days)",
        "late_postpartum": "Late (43+ days)"
    }.get(profile['phase'], "Early (8–42 days)")

    phase_options = list(PHASE_KEY_MAP.keys())
    default_index = phase_options.index(current_phase_label) if current_phase_label in phase_options else 1

    st.info(t("nutrition_message", lang).format(name=profile['name'], phase=current_phase_label))

    phase_label = st.selectbox(t("postpartum_phase", lang), phase_options, index=default_index)
    symptoms_text = st.text_input(t("symptoms_optional", lang), placeholder="e.g., constipation, low energy...")
    days_pp = st.number_input(t("days_postpartum", lang), min_value=0, max_value=365, value=profile['postpartum_days'], key="nutrition_days")

    # Audio input for nutrition
    st.markdown("**🎤 Or describe dietary needs/symptoms with voice**")
    audio_bytes_nutrition = mic_recorder(
        start_prompt="🎙️ Record",
        stop_prompt="⏹️ Stop",
        just_once=False,
        use_container_width=False,
        key="nutrition_audio"
    )

    if audio_bytes_nutrition:
        temp_dir = Path(tempfile.gettempdir()) / "ira_audio"
        temp_dir.mkdir(exist_ok=True)
        audio_path_nutrition = temp_dir / f"nutrition_{profile['name']}.wav"

        with open(audio_path_nutrition, "wb") as f:
            f.write(audio_bytes_nutrition['bytes'])

        st.audio(audio_bytes_nutrition['bytes'], format='audio/wav')

        with st.spinner("🎧 Transcribing..."):
            transcription_nutrition = transcribe_audio_with_gemma(gemma_client, str(audio_path_nutrition), lang)

        if transcription_nutrition and not transcription_nutrition.startswith("[Audio transcription error"):
            st.success("✅ Voice message transcribed!")
            st.info(f"**You said:** {transcription_nutrition}")
            if symptoms_text:
                symptoms_text = f"{symptoms_text}, {transcription_nutrition}"
            else:
                symptoms_text = transcription_nutrition

    if st.button(t("get_diet_plan", lang)):
        # Parse symptoms
        symptom_list = [s.strip() for s in symptoms_text.split(",") if s.strip()]
        if not symptom_list and symptoms_text.strip():
            symptom_list = [symptoms_text.strip()]

        # Map phase
        phase_key = PHASE_KEY_MAP[phase_label]

        try:
            with st.spinner(t("preparing_diet_plan", lang)):
                flow = PostpartumFlow(dm=dataset_manager, gc=gemma_client)
                flow.kickoff(inputs={
                    "symptoms":        symptom_list,
                    "days_postpartum": int(days_pp),
                    "language":        st.session_state.language,
                    "phase":           phase_key,
                    "journal_text":    "",
                    "audio_path":      "",
                })

            state = flow.state

            if state.is_emergency:
                st.error(state.safety_result)
                st.stop()

            st.markdown(t("your_diet_plan", lang))
            if state.diet_result:
                st.write(state.diet_result)
            else:
                st.warning(t("could_not_generate_diet", lang))

            if state.triage_result:
                with st.expander(t("health_guidance", lang)):
                    st.write(state.triage_result)
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.warning("Please try again later.")


# ── Journal ───────────────────────────────────────────────────────────────────

elif page == "My Journal":
    lang = st.session_state.language
    st.subheader(t("journal_title", lang))
    st.caption(t("journal_caption", lang))

    col1, col2 = st.columns([3, 1])
    with col1:
        text = st.text_area(t("placeholder_journal", lang), height=150, key="journal_text_input")
    with col2:
        analyze_entry = st.checkbox(t("get_ai_analysis", lang), value=True)

    # Audio journal entry
    st.markdown("---")
    st.markdown("**🎤 Or record a voice journal entry**")
    audio_bytes_journal = mic_recorder(
        start_prompt="🎙️ Start Recording",
        stop_prompt="⏹️ Stop Recording",
        just_once=False,
        use_container_width=False,
        key="journal_audio"
    )

    if audio_bytes_journal:
        temp_dir = Path(tempfile.gettempdir()) / "ira_audio"
        temp_dir.mkdir(exist_ok=True)
        audio_path_journal = temp_dir / f"journal_{profile['name']}.wav"

        with open(audio_path_journal, "wb") as f:
            f.write(audio_bytes_journal['bytes'])

        st.audio(audio_bytes_journal['bytes'], format='audio/wav')

        with st.spinner("🎧 Transcribing your journal entry..."):
            transcription_journal = transcribe_audio_with_gemma(gemma_client, str(audio_path_journal), lang)

        if transcription_journal and not transcription_journal.startswith("[Audio transcription error"):
            st.success("✅ Voice journal transcribed!")
            st.info(f"**Your journal:** {transcription_journal}")
            if text:
                text = f"{text}\n\n[Voice entry]: {transcription_journal}"
            else:
                text = transcription_journal

    if st.button(t("save_entry", lang), type="primary"):
        if not text.strip():
            st.warning(t("please_write_something", lang))
            st.stop()

        if "journal_entries" not in st.session_state:
            st.session_state.journal_entries = []

        import datetime

        entry_data = {
            "text":      text,
            "language":  st.session_state.language,
            "timestamp": datetime.datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "analysis":  None,
        }

        # AI analysis if requested
        if analyze_entry:
            try:
                with st.spinner(t("analyzing_entry", lang)):
                    flow = PostpartumFlow(dm=dataset_manager, gc=gemma_client)
                    flow.kickoff(inputs={
                        "symptoms":        [],
                        "days_postpartum": 0,
                        "language":        st.session_state.language,
                        "phase":           "early_postpartum",
                        "journal_text":    text,
                        "audio_path":      "",
                    })
                    if flow.state.journal_result:
                        entry_data["analysis"] = flow.state.journal_result
            except Exception as e:
                st.warning(t("error_generic", lang).format(error=str(e)))

        st.session_state.journal_entries.append(entry_data)

        # Show analysis immediately
        if entry_data.get("analysis"):
            st.markdown(t("emotional_analysis", lang))
            st.info(entry_data["analysis"])

            # Check for PPD signals
            if "ppd" in entry_data["analysis"].lower() or "high" in entry_data["analysis"].lower():
                st.warning(t("ppd_warning", lang))

        st.success(t("entry_saved", lang))
        st.rerun()

    # ── Past entries — read only ──────────────────────────────────────────────
    if "journal_entries" in st.session_state and st.session_state.journal_entries:
        st.markdown(t("your_entries", lang))
        for entry in reversed(st.session_state.journal_entries):
            with st.container(border=True):
                st.caption(entry["timestamp"])
                st.write(entry["text"])
                if entry.get("analysis"):
                    with st.expander(t("view_analysis", lang)):
                        st.info(entry["analysis"])
# ── Feed ──────────────────────────────────────────────────────────────────────

elif page == "Articles":
    lang = st.session_state.language
    st.subheader(t("trusted_articles", lang))

    from app.source_registry import TRUSTED_SOURCES, KNOWLEDGE_BASE_REFERENCES

    st.markdown(t("live_feeds", lang))
    for source in [s for s in TRUSTED_SOURCES if s["source_type"] == "rss"]:
        st.markdown(f"**{source['source_name']}**")
        st.markdown(f"[{source['url']}]({source['url']})")
        st.caption(", ".join(source.get("topic_tags", [])))
        st.divider()

    st.markdown(t("clinical_references", lang))
    for ref in KNOWLEDGE_BASE_REFERENCES:
        st.markdown(f"**{ref['source_name']}**")
        st.markdown(f"[Read →]({ref['url']})")
        if "key_insight" in ref:
            st.caption(ref["key_insight"])
        st.divider()

# ── Community ──────────────────────────────────────────────────────────────────────
elif page == "Mom's Circle":
    lang = st.session_state.language
    from app.community import get_all_tips, post_tip, post_reply, like_tip

    st.subheader(t("community_tips", lang))
    st.caption(t("community_caption", lang))

    # ── Post a new tip ────────────────────────────────────────────────────────
    with st.expander(t("share_tip", lang), expanded=True):
        author  = st.text_input(f"{t('your_name', lang)} (optional)", placeholder=t("placeholder_name", lang))
        tip_text = st.text_area(t("your_tip", lang), placeholder="e.g. Drinking ajwain water really helped with my digestion...")

        # Audio tip
        st.markdown("**🎤 Or record your tip with voice**")
        audio_bytes_tip = mic_recorder(
            start_prompt="🎙️ Record Tip",
            stop_prompt="⏹️ Stop",
            just_once=False,
            use_container_width=False,
            key="community_tip_audio"
        )

        if audio_bytes_tip:
            temp_dir = Path(tempfile.gettempdir()) / "ira_audio"
            temp_dir.mkdir(exist_ok=True)
            audio_path_tip = temp_dir / f"tip_{author or 'anonymous'}.wav"

            with open(audio_path_tip, "wb") as f:
                f.write(audio_bytes_tip['bytes'])

            st.audio(audio_bytes_tip['bytes'], format='audio/wav')

            with st.spinner("🎧 Transcribing your tip..."):
                transcription_tip = transcribe_audio_with_gemma(gemma_client, str(audio_path_tip), lang)

            if transcription_tip and not transcription_tip.startswith("[Audio transcription error"):
                st.success("✅ Voice tip transcribed!")
                st.info(f"**Your tip:** {transcription_tip}")
                if tip_text:
                    tip_text = f"{tip_text}\n\n[Voice tip]: {transcription_tip}"
                else:
                    tip_text = transcription_tip

        if st.button(t("post_tip", lang), type="primary"):
            if not tip_text.strip():
                st.warning(t("please_write_tip", lang))
            else:
                try:
                    post_tip(
                        author=author,
                        language=st.session_state.language,
                        text=tip_text,
                    )
                    st.success(t("tip_posted", lang))
                    st.rerun()
                except ValueError as e:
                    st.error(t("could_not_post", lang).format(error=str(e)))
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")

    st.divider()

    # ── Display all tips ──────────────────────────────────────────────────────
    tips = get_all_tips()

    if not tips:
        st.info(t("no_tips_yet", lang))
    else:
        for tip in tips:
            with st.container(border=True):
                col1, col2 = st.columns([5, 1])

                with col1:
                    st.markdown(f"**{tip['author']}** · {tip['timestamp']}")
                    st.write(tip["text"])

                with col2:
                    if st.button(f"❤️ {tip['likes']}", key=f"like_{tip['id']}"):
                        like_tip(tip["id"])
                        st.rerun()

                # ── Replies ───────────────────────────────────────────────────
                if tip["replies"]:
                    with st.expander(f"💬 {len(tip['replies'])} repl{'y' if len(tip['replies']) == 1 else 'ies'}"):
                        for reply in tip["replies"]:
                            st.markdown(f"↳ **{reply['author']}** · {reply['timestamp']}")
                            st.write(reply["text"])

                # ── Reply form ────────────────────────────────────────────────
                with st.expander(t("reply", lang)):
                    reply_author = st.text_input(
                        t("your_name", lang),
                        placeholder=t("placeholder_name", lang),
                        key=f"reply_author_{tip['id']}"
                    )
                    reply_text = st.text_area(
                        t("your_reply", lang),
                        placeholder="Write your reply...",
                        key=f"reply_text_{tip['id']}"
                    )
                    if st.button(t("post_reply", lang), key=f"reply_btn_{tip['id']}"):
                        if not reply_text.strip():
                            st.warning(t("please_write_tip", lang))
                        else:
                            try:
                                post_reply(
                                    tip_id=tip["id"],
                                    author=reply_author,
                                    text=reply_text,
                                )
                                st.success(t("reply_posted", lang))
                                st.rerun()
                            except ValueError as e:
                                st.error(t("could_not_post", lang).format(error=str(e)))
                            except Exception as e:
                                st.error(f"❌ An error occurred: {str(e)}")

elif page == "Track Your Health":
    lang = st.session_state.language
    st.subheader(t("health_tracker", lang))
    st.caption(t("tracker_caption", lang))

    import pandas as pd

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        t("tab_bp_sugar", lang),
        t("tab_vitals", lang),
        t("tab_sleep", lang),
        t("tab_cycle", lang),
        t("tab_pregnancy", lang),
        t("tab_history", lang),
    ])

    # shared entry dict built across tabs
    if "tracker_entry" not in st.session_state:
        st.session_state.tracker_entry = {}

    # ── Tab 1: BP & Sugar ─────────────────────────────────────────────────────
    with tab1:
        st.markdown(t("blood_pressure", lang))
        col1, col2 = st.columns(2)
        with col1:
            bp_sys = st.number_input(t("systolic", lang), 0, 300, 0, key="bp_sys")
        with col2:
            bp_dia = st.number_input(t("diastolic", lang), 0, 200, 0, key="bp_dia")

        st.markdown(t("blood_sugar", lang))
        col3, col4, col5 = st.columns(3)
        with col3:
            sugar_normal = st.number_input(t("sugar_normal", lang), 0.0, 600.0, 0.0, key="s_normal")
        with col4:
            sugar_fasting = st.number_input(t("sugar_fasting", lang), 0.0, 600.0, 0.0, key="s_fasting")
        with col5:
            sugar_pp = st.number_input(t("sugar_pp", lang), 0.0, 600.0, 0.0, key="s_pp")

        st.session_state.tracker_entry.update({
            "bp_systolic":        bp_sys  if bp_sys  > 0 else None,
            "bp_diastolic":       bp_dia  if bp_dia  > 0 else None,
            "sugar_normal":       sugar_normal   if sugar_normal   > 0 else None,
            "sugar_fasting":      sugar_fasting  if sugar_fasting  > 0 else None,
            "sugar_postprandial": sugar_pp       if sugar_pp       > 0 else None,
        })

    # ── Tab 2: Vitals ─────────────────────────────────────────────────────────
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            temp       = st.number_input(t("temperature", lang), 0.0, 45.0, 0.0, key="temp")
            heart_rate = st.number_input(t("heart_rate", lang), 0, 250, 0, key="hr")
            blood_o2   = st.number_input(t("blood_oxygen", lang), 0, 100, 0, key="spo2")
        with col2:
            weight     = st.number_input(t("weight", lang), 0.0, 200.0, 0.0, key="weight")
            thyroid    = st.number_input(t("thyroid_tsh", lang), 0.0, 100.0, 0.0, key="tsh")
            hydration  = st.number_input(t("hydration", lang), 0, 20, 0, key="hydration")

        mood = st.select_slider(
            t("mood_today", lang),
            options=["😢 Very Low", "😔 Low", "😐 Okay", "🙂 Good", "😊 Great"],
            key="mood"
        )

        st.session_state.tracker_entry.update({
            "temperature":       temp       if temp       > 0 else None,
            "heart_rate":        heart_rate if heart_rate > 0 else None,
            "blood_oxygen":      blood_o2   if blood_o2   > 0 else None,
            "weight":            weight     if weight     > 0 else None,
            "thyroid_tsh":       thyroid    if thyroid    > 0 else None,
            "hydration_glasses": hydration  if hydration  > 0 else None,
            "mood":              mood,
        })

    # ── Tab 3: Sleep ──────────────────────────────────────────────────────────
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            sleep_hours = st.number_input(t("sleep_duration", lang), 0.0, 24.0, 0.0, key="sleep_h")
            sleep_quality = st.select_slider(
                t("sleep_quality", lang),
                options=["Very Poor", "Poor", "Fair", "Good", "Excellent"],
                key="sleep_q"
            )
        with col2:
            sleep_stage = st.multiselect(
                t("sleep_stages", lang),
                ["Light sleep", "Deep sleep", "REM sleep", "Interrupted"],
                key="sleep_s"
            )

        st.session_state.tracker_entry.update({
            "sleep_hours":   sleep_hours  if sleep_hours > 0 else None,
            "sleep_quality": sleep_quality,
            "sleep_stages":  ", ".join(sleep_stage) if sleep_stage else None,
        })

    # ── Tab 4: Cycle ──────────────────────────────────────────────────────────
    with tab4:
        st.markdown(t("period_log", lang))
        period_status = st.selectbox(
            t("period_status", lang),
            ["Not started", "Started", "Ongoing", "Ended", "Irregular", "Spotting"],
            key="period_status"
        )
        flow_intensity = st.select_slider(
            t("flow_intensity", lang),
            options=["None", "Spotting", "Light", "Medium", "Heavy"],
            key="flow"
        ) if period_status not in ["Not started", "Ended"] else None

        st.markdown(t("discharge_section", lang))
        discharge = st.selectbox(
            t("discharge_type", lang),
            ["None", "Clear/White (normal)", "Yellow", "Green", "Brown",
             "Pink tinged", "Heavy/Unusual"],
            key="discharge"
        )

        st.markdown(t("fertile_days", lang))
        fertile = st.checkbox(t("fertile_day", lang), key="fertile")
        ovulation = st.checkbox(t("ovulation", lang), key="ovulation")

        st.session_state.tracker_entry.update({
            "period_status":   period_status,
            "flow_intensity":  flow_intensity,
            "discharge":       discharge,
            "fertile_day":     fertile,
            "ovulation":       ovulation,
        })

    # ── Tab 5: Pregnancy ──────────────────────────────────────────────────────
    with tab5:
        st.markdown(t("pregnancy_log", lang))
        preg_week = st.number_input(t("pregnancy_week", lang), 0, 42, 0, key="preg_week")
        preg_symptoms = st.multiselect(
            t("pregnancy_symptoms", lang),
            ["Nausea", "Vomiting", "Headache", "Back pain", "Swelling",
             "Cramps", "Spotting", "Fatigue", "Heartburn", "Baby movement felt"],
            key="preg_symptoms"
        )
        preg_weight = st.number_input(t("pregnancy_weight", lang), 0.0, 200.0, 0.0, key="preg_weight")
        preg_notes  = st.text_area(t("pregnancy_notes", lang), key="preg_notes")

        st.session_state.tracker_entry.update({
            "pregnancy_week":     preg_week    if preg_week > 0 else None,
            "pregnancy_symptoms": ", ".join(preg_symptoms) if preg_symptoms else None,
            "pregnancy_weight":   preg_weight  if preg_weight > 0 else None,
            "pregnancy_notes":    preg_notes   if preg_notes.strip() else None,
        })

    # ── Save button (outside tabs, applies to all) ────────────────────────────
    lang = st.session_state.language
    st.divider()
    notes = st.text_area(f"{t('notes', lang)} (optional)", key="general_notes")
    st.session_state.tracker_entry["notes"] = notes or None

    if st.button(t("save_all_readings", lang), type="primary"):
        flow = PostpartumFlow(dm=dataset_manager, gc=gemma_client)
        flow.state.language = st.session_state.language

        with st.spinner(t("saving_readings", lang)):
            result = flow.run_tracker(st.session_state.tracker_entry.copy())

        # Check for validation errors first
        if result.get("errors"):
            st.error(t("invalid_values", lang))
            for error in result["errors"]:
                st.error(f"  • {error}")
            st.warning(t("correct_values", lang))
        elif result["alerts"]:
            st.warning(t("health_alerts", lang))
            for alert in result["alerts"]:
                st.warning(alert)
            if result.get("summary"):
                with st.expander(t("ai_analysis", lang), expanded=True):
                    st.info(result["summary"])
            st.success(t("readings_saved", lang))
            # clear after save
            st.session_state.tracker_entry = {}
            st.rerun()
        else:
            st.success(t("all_good", lang))
            # clear after save
            st.session_state.tracker_entry = {}
            st.rerun()

    # ── Tab 6: History ────────────────────────────────────────────────────────
    with tab6:
        flow_h  = PostpartumFlow(dm=dataset_manager, gc=gemma_client)
        entries = flow_h.get_tracker_history()

        if not entries:
            st.info(t("no_entries", lang))
        else:
            df = pd.DataFrame(entries)

            col1, col2 = st.columns(2)

            with col1:
                bp_df = df[df["bp_systolic"].notna()][["date", "bp_systolic", "bp_diastolic"]]
                if not bp_df.empty:
                    st.markdown("**🩸 Blood Pressure**")
                    st.line_chart(bp_df.set_index("date"))

                sugar_df = df[df["sugar_fasting"].notna()][["date", "sugar_fasting", "sugar_postprandial"]]
                if not sugar_df.empty:
                    st.markdown("**🍬 Blood Sugar**")
                    st.line_chart(sugar_df.set_index("date"))

                oxygen_df = df[df["blood_oxygen"].notna()][["date", "blood_oxygen"]]
                if not oxygen_df.empty:
                    st.markdown("**🫁 Blood Oxygen**")
                    st.line_chart(oxygen_df.set_index("date"))

            with col2:
                sleep_df = df[df["sleep_hours"].notna()][["date", "sleep_hours"]]
                if not sleep_df.empty:
                    st.markdown("**🌙 Sleep**")
                    st.line_chart(sleep_df.set_index("date"))

                weight_df = df[df["weight"].notna()][["date", "weight"]]
                if not weight_df.empty:
                    st.markdown("**⚖️ Weight**")
                    st.line_chart(weight_df.set_index("date"))

                thyroid_df = df[df["thyroid_tsh"].notna()][["date", "thyroid_tsh"]]
                if not thyroid_df.empty:
                    st.markdown("**🔬 Thyroid TSH**")
                    st.line_chart(thyroid_df.set_index("date"))

            with st.expander("📋 Full history table"):
                display_cols = [
                    c for c in [
                        "timestamp", "bp_systolic", "bp_diastolic",
                        "sugar_normal", "sugar_fasting", "sugar_postprandial",
                        "temperature", "heart_rate", "blood_oxygen",
                        "weight", "thyroid_tsh", "hydration_glasses",
                        "sleep_hours", "sleep_quality",
                        "period_status", "discharge", "mood", "notes"
                    ] if c in df.columns
                ]
                st.dataframe(df[display_cols], use_container_width=True)

# ── Chatbot page ──────────────────────────────────────────────────────────────

elif page == "🔍 Health Insights":
    from app.streamlit_insights import render_insights_page
    render_insights_page(gemma_client, dataset_manager, st.session_state.user_profile)

elif page == "Share with Ira":
    lang = st.session_state.language
    st.subheader(t("share_with_ira", lang))
    st.caption(t("chat_caption", lang))

    profile = st.session_state.user_profile

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # greeting
    if not st.session_state.chat_history:
        with st.chat_message("assistant", avatar="🌸"):
            # Personalized greeting
            greeting = t("ira_greeting", lang).format(name=profile['name']) + " "

            if profile['postpartum_days'] <= 7:
                greeting += "Congratulations on your new baby! These first days are so precious and can also be challenging. "
            elif profile['postpartum_days'] <= 42:
                greeting += f"You're doing amazing — {profile['postpartum_days']} days into your postpartum journey! "
            else:
                greeting += "You've come so far in your recovery journey! "

            greeting += "I'm here to listen, support, and help with anything on your mind. How are you feeling today?"

            st.write(greeting)

    # display history
    for turn in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(turn["user"])
        with st.chat_message("assistant", avatar="🌸"):
            st.write(turn["ira"])

    # Audio input for chat
    st.markdown("**🎤 Record a voice message to Ira**")
    audio_bytes_chat = mic_recorder(
        start_prompt="🎙️ Talk to Ira",
        stop_prompt="⏹️ Stop",
        just_once=False,
        use_container_width=False,
        key="chat_audio"
    )

    user_input = None

    if audio_bytes_chat:
        temp_dir = Path(tempfile.gettempdir()) / "ira_audio"
        temp_dir.mkdir(exist_ok=True)
        audio_path_chat = temp_dir / f"chat_{profile['name']}.wav"

        with open(audio_path_chat, "wb") as f:
            f.write(audio_bytes_chat['bytes'])

        st.audio(audio_bytes_chat['bytes'], format='audio/wav')

        with st.spinner("🎧 Listening to your message..."):
            user_input = transcribe_audio_with_gemma(gemma_client, str(audio_path_chat), lang)

        if user_input and not user_input.startswith("[Audio transcription error"):
            st.success(f"✅ **You said:** {user_input}")

    # Text input
    if not user_input:
        user_input = st.chat_input(t("type_message", lang))

    if user_input:
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant", avatar="🌸"):
            try:
                with st.spinner(t("ira_typing", lang)):
                    # Check if user wants to use a tool
                    tool_keywords = ["remind", "schedule", "show trend", "my bp", "my sleep", "generate report"]
                    use_tools = any(kw in user_input.lower() for kw in tool_keywords)

                    if use_tools:
                        # Try function calling
                        from app.tools_registry import AVAILABLE_TOOLS, execute_tool
                        result = gemma_client.generate_with_tools(
                            user_prompt=user_input,
                            tools=AVAILABLE_TOOLS,
                            system_prompt="You are Ira, a helpful postpartum care assistant with access to health tracking tools."
                        )

                        if result.get("tool"):
                            # Execute tool
                            tool_result = execute_tool(
                                result["tool"],
                                result.get("parameters", {}),
                                context={"tracker_data": flow.get_tracker_history()}
                            )

                            # Generate response based on tool result
                            response = f"✅ {tool_result.get('message', json.dumps(tool_result, indent=2))}"
                        else:
                            response = result.get("response", "I'm not sure how to help with that.")
                    else:
                        # Regular chat
                        flow = PostpartumFlow(dm=dataset_manager, gc=gemma_client)
                        flow.state.language = st.session_state.language
                        response = flow.chat(
                            user_message=user_input,
                            history=st.session_state.chat_history,
                            language=st.session_state.language,
                            user_context=profile,
                        )

                st.write(response)
            except Exception as e:
                response = f"I'm sorry, I'm having trouble responding right now. Please try again. (Error: {str(e)})"
                st.error(response)

        st.session_state.chat_history.append({
            "user": user_input,
            "ira":  response,
        })

    if st.session_state.chat_history:
        if st.button(t("clear_conversation", lang)):
            st.session_state.chat_history = []
            st.rerun()
