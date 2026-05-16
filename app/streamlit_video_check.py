"""Video Health Check page - Video analysis with Gemma 4."""

import streamlit as st
from pathlib import Path
import tempfile


def render_video_check_page(gemma_client, user_profile):
    """Render the Video Health Check page."""
    st.subheader("🎥 Video Health Check")
    st.caption("Upload videos for AI-powered analysis")

    st.info(
        "⚕️ **Medical Disclaimer**: This is a preliminary AI assessment only. "
        "Always consult your healthcare provider for accurate diagnosis and treatment."
    )

    # Video type selector
    video_type = st.selectbox(
        "What would you like to analyze?",
        [
            "👶 Baby Movement & Development",
            "🤸‍♀️ Exercise Form Check",
            "💤 Sleep Pattern Analysis",
            "🍼 Feeding Session",
            "👨‍👩‍👧 Parent-Baby Interaction",
            "🏃‍♀️ Physical Activity",
            "Other"
        ]
    )

    # Video upload
    uploaded_video = st.file_uploader(
        "Upload video",
        type=["mp4", "avi", "mov", "mkv"],
        help="Maximum file size: 50MB, Duration: Max 2 minutes recommended"
    )

    if uploaded_video:
        # Validate size
        if uploaded_video.size > 50 * 1024 * 1024:
            st.error("❌ Video too large. Maximum size: 50MB")
            return

        # Display video
        col1, col2 = st.columns([2, 1])

        with col1:
            st.video(uploaded_video)

        with col2:
            # Additional context
            additional_info = st.text_area(
                "Additional information (optional)",
                placeholder="e.g., Baby is 3 weeks old, this is typical behavior...",
                height=100,
                key="video_context"
            )

            # Sampling rate
            sample_fps = st.slider(
                "Analysis detail",
                min_value=0.5,
                max_value=2.0,
                value=1.0,
                step=0.5,
                help="Higher = more frames analyzed (slower)"
            )

            # Analysis settings
            show_thinking = st.checkbox("Show AI reasoning", value=False, key="video_thinking")

        # Analyze button
        if st.button("🔍 Analyze Video", type="primary", use_container_width=True):
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                tmp_file.write(uploaded_video.read())
                temp_path = tmp_file.name

            # Build prompt based on video type
            prompts = {
                "👶 Baby Movement & Development": """
                    Analyze this baby's movements and development. Look for:
                    - Motor skill milestones (head control, limb movement, reflexes)
                    - General activity level and responsiveness
                    - Any concerning patterns or delays
                    - Age-appropriate development signs
                    Provide supportive, non-alarmist feedback for the mother.
                """,
                "🤸‍♀️ Exercise Form Check": """
                    Analyze this postpartum exercise form. Check for:
                    - Proper alignment and posture
                    - Core engagement and pelvic floor safety
                    - Movements to avoid or modify
                    - Form corrections and safety tips
                    Be encouraging and supportive in your feedback.
                """,
                "💤 Sleep Pattern Analysis": """
                    Analyze sleep patterns visible in this video. Look for:
                    - Sleep quality indicators
                    - Positioning and safety
                    - Restlessness or disturbances
                    - Environmental factors
                    Provide gentle suggestions for improvement.
                """,
                "🍼 Feeding Session": """
                    Analyze this feeding session. Observe:
                    - Baby's latch and positioning (if breastfeeding)
                    - Feeding cues and responsiveness
                    - Mother-baby coordination
                    - Potential issues or concerns
                    Offer supportive guidance and tips.
                """,
                "👨‍👩‍👧 Parent-Baby Interaction": """
                    Analyze parent-baby bonding and interaction. Look for:
                    - Responsiveness and engagement
                    - Bonding indicators
                    - Communication patterns
                    - Positive interaction moments
                    Highlight strengths and gentle suggestions.
                """,
                "🏃‍♀️ Physical Activity": """
                    Analyze this physical activity for postpartum safety. Check:
                    - Movement intensity and impact
                    - Core and pelvic floor stress
                    - Recovery-appropriate exercises
                    - Red flags or modifications needed
                    Provide safe exercise guidance.
                """,
                "Other": "Analyze this video in the context of postpartum health and provide relevant insights."
            }

            prompt = prompts.get(video_type, prompts["Other"])
            if additional_info:
                prompt += f"\n\nAdditional context: {additional_info}"

            with st.spinner("Analyzing video... This may take 30-60 seconds."):
                try:
                    if show_thinking:
                        # For thinking mode, analyze frames then add reasoning
                        result = gemma_client.generate_with_thinking(
                            system_prompt="You are a compassionate postpartum health AI assistant with expertise in maternal and infant care.",
                            user_prompt=f"Video analysis request: {prompt}\n\nNote: Multiple frames from the video will be provided for analysis."
                        )

                        st.markdown("### 🧠 AI Reasoning Process")
                        with st.expander("How Ira analyzed this video", expanded=False):
                            st.write(result["thinking"])

                        st.markdown("### 📋 Analysis")
                        st.write(result["answer"])

                    else:
                        # Direct video analysis
                        response = gemma_client.generate_with_video(
                            video_path=temp_path,
                            prompt=prompt,
                            system_prompt="You are Ira, a compassionate postpartum health AI assistant with maternal and infant care expertise.",
                            max_new_tokens=800,
                            sample_fps=sample_fps
                        )

                        st.markdown("### 📋 Video Analysis")
                        st.write(response)

                    # Warning footer
                    st.warning(
                        "⚠️ **Important**: This is a preliminary AI assessment based on video frames. "
                        "Please consult your healthcare provider for proper diagnosis and guidance. "
                        "If you notice concerning symptoms, seek medical attention immediately."
                    )

                    # Export option
                    st.markdown("---")
                    if st.button("📤 Export Analysis"):
                        import datetime
                        export_text = f"""
Video Health Check Report
Generated: {datetime.datetime.now().strftime('%d %b %Y, %I:%M %p')}

Patient: {user_profile.get('name')}
Days Postpartum: {user_profile.get('postpartum_days')}
Video Type: {video_type}

Additional Info: {additional_info or 'None provided'}

AI Analysis:
{response if not show_thinking else result['answer']}

---
Note: This is an AI-generated preliminary assessment. Professional medical evaluation is required.
"""
                        st.download_button(
                            "📥 Download Report",
                            data=export_text,
                            file_name=f"video_check_{video_type.replace(' ', '_')}.txt",
                            mime="text/plain"
                        )

                    # Clean up temp file
                    try:
                        Path(temp_path).unlink()
                    except:
                        pass

                except Exception as e:
                    st.error(f"❌ Analysis failed: {str(e)}")
                    st.info("💡 Make sure opencv-python is installed: `pip install opencv-python`")
                    st.warning("Please try again or consult your healthcare provider directly.")

    # Educational section
    st.markdown("---")
    with st.expander("ℹ️ What can Video Health Check help with?"):
        st.markdown("""
**This feature can provide preliminary insights for:**

✅ **Baby Development**: Track motor skills, reflexes, activity levels
✅ **Exercise Safety**: Check postpartum exercise form and safety
✅ **Sleep Patterns**: Analyze sleep quality and positioning
✅ **Feeding Sessions**: Assess breastfeeding latch and positioning
✅ **Bonding**: Observe parent-baby interaction patterns
✅ **Physical Activity**: Ensure recovery-safe movements

**How it works:**
- Video is sampled into frames (typically 8-10 frames)
- AI analyzes each frame for patterns and movements
- Comprehensive assessment across entire video duration
- Context-aware analysis based on postpartum care

**Best practices:**
- Keep videos under 2 minutes for best results
- Ensure good lighting and clear view
- Hold camera steady if possible
- Include relevant context in description

**Limitations:**
- AI cannot diagnose medical conditions
- Cannot replace professional assessment
- May miss subtle details
- Not suitable for emergency situations

**When to see a doctor immediately:**
- Baby shows no movement or weak movements
- Severe pain during exercise
- Any concerning developmental delays
- Signs of distress in baby or mother
""")

    # Tips section
    with st.expander("📹 Video Recording Tips"):
        st.markdown("""
**For Baby Development Videos:**
- Record during active/awake time
- 30-60 seconds is usually enough
- Show full body movement
- Natural lighting works best

**For Exercise Form:**
- Record full body if possible
- Side view and front view both helpful
- Perform 3-5 reps of the exercise
- Clear, uncluttered background

**For Sleep Analysis:**
- Use night vision or dim light
- Record 1-2 minutes of sleep
- Include positioning and environment
- Respect privacy - only upload what you're comfortable with

**General Tips:**
- Hold phone horizontally (landscape)
- Keep camera steady
- Avoid zooming during recording
- Ensure subject is well-lit and visible
""")
