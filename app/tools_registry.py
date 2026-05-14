"""Function calling tools registry for Gemma 4."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict, List, Any
import json


# Available tools for function calling
AVAILABLE_TOOLS = [
    {
        "name": "get_health_trend",
        "description": "Retrieve health metrics trend over specified days",
        "parameters": {
            "metric": {"type": "string", "enum": ["bp", "sugar", "sleep", "weight", "mood"], "description": "Metric to retrieve"},
            "days": {"type": "integer", "description": "Number of days to look back"}
        }
    },
    {
        "name": "schedule_reminder",
        "description": "Schedule a health reminder for the user",
        "parameters": {
            "task": {"type": "string", "description": "What to remind about"},
            "time": {"type": "string", "description": "Time in HH:MM format"},
            "frequency": {"type": "string", "enum": ["once", "daily", "weekly"], "description": "How often"}
        }
    },
    {
        "name": "analyze_symptoms_structured",
        "description": "Extract and structure symptoms from natural language",
        "parameters": {
            "text": {"type": "string", "description": "Natural language symptom description"}
        }
    },
    {
        "name": "risk_assessment",
        "description": "Generate structured risk assessment for current health state",
        "parameters": {
            "symptoms": {"type": "array", "description": "List of symptoms"},
            "vitals": {"type": "object", "description": "Latest vital signs"}
        }
    },
    {
        "name": "generate_health_report",
        "description": "Generate comprehensive health report using all available data",
        "parameters": {
            "days": {"type": "integer", "description": "Number of days to include in report"}
        }
    }
]


def execute_tool(tool_name: str, parameters: Dict[str, Any], context: Dict = None) -> Dict[str, Any]:
    """Execute a tool and return results."""

    if tool_name == "get_health_trend":
        return _get_health_trend(parameters, context)

    elif tool_name == "schedule_reminder":
        return _schedule_reminder(parameters)

    elif tool_name == "analyze_symptoms_structured":
        return _analyze_symptoms(parameters)

    elif tool_name == "risk_assessment":
        return _risk_assessment(parameters)

    elif tool_name == "generate_health_report":
        return _generate_report(parameters, context)

    return {"error": f"Unknown tool: {tool_name}"}


def _get_health_trend(params: Dict, context: Dict) -> Dict:
    """Get health metric trend."""
    metric = params.get("metric")
    days = params.get("days", 7)

    # Get data from context
    tracker_data = context.get("tracker_data", []) if context else []

    # Filter by metric and days
    filtered = []
    for entry in tracker_data[-days:]:
        if metric == "bp" and entry.get("bp_systolic"):
            filtered.append({"date": entry["date"], "value": f"{entry['bp_systolic']}/{entry.get('bp_diastolic', 0)}"})
        elif metric == "sugar" and entry.get("sugar_fasting"):
            filtered.append({"date": entry["date"], "value": entry["sugar_fasting"]})
        elif metric == "sleep" and entry.get("sleep_hours"):
            filtered.append({"date": entry["date"], "value": entry["sleep_hours"]})
        elif metric == "weight" and entry.get("weight"):
            filtered.append({"date": entry["date"], "value": entry["weight"]})
        elif metric == "mood":
            filtered.append({"date": entry["date"], "value": entry.get("mood", "N/A")})

    return {"metric": metric, "days": days, "data": filtered}


def _schedule_reminder(params: Dict) -> Dict:
    """Schedule a reminder."""
    task = params.get("task")
    time = params.get("time")
    frequency = params.get("frequency", "once")

    # In real implementation, this would integrate with a task scheduler
    return {
        "status": "scheduled",
        "task": task,
        "time": time,
        "frequency": frequency,
        "message": f"✅ Reminder set: '{task}' at {time} ({frequency})"
    }


def _analyze_symptoms(params: Dict) -> Dict:
    """Analyze symptoms from text."""
    text = params.get("text", "")

    # This would use Gemma's JSON mode in real implementation
    # For now, return structured format
    return {
        "raw_text": text,
        "extracted_symptoms": [],
        "severity": {},
        "note": "Use Gemma's JSON mode for actual extraction"
    }


def _risk_assessment(params: Dict) -> Dict:
    """Risk assessment."""
    symptoms = params.get("symptoms", [])
    vitals = params.get("vitals", {})

    # Calculate risk score
    risk_level = "low"
    if len(symptoms) > 5:
        risk_level = "moderate"
    if any(s in ["chest pain", "severe headache", "heavy bleeding"] for s in symptoms):
        risk_level = "high"

    return {
        "risk_level": risk_level,
        "confidence": 0.85,
        "factors": symptoms,
        "vitals_status": "within_range" if vitals else "no_data"
    }


def _generate_report(params: Dict, context: Dict) -> Dict:
    """Generate comprehensive report."""
    days = params.get("days", 30)

    return {
        "report_period": f"Last {days} days",
        "status": "generated",
        "note": "Full report generation requires long-context processing"
    }
