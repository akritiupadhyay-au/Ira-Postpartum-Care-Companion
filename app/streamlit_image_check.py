"""Visual Health Check page - Image analysis with Gemma 4."""

import streamlit as st
from pathlib import Path
from PIL import Image


def render_image_check_page(gemma_client, user_profile):
    """Render the Visual Health Check page."""
    st.subheader("📸 Visual Health Check")
    st.caption("Upload photos for AI-powered preliminary assessment")

    st.info(
        "⚕️ **Medical Disclaimer**: This is a preliminary AI assessment only. "
        "Always consult your healthcare provider for accurate diagnosis and treatment."
    )

    # Check type selector
    check_type = st.selectbox(
        "What would you like to check?",
        [
            "Skin condition / Rash",
            "C-section scar healing",
            "Breast condition",
            "Baby's diaper (check for abnormalities)",
            "Medicine verification",
            "Food / Meal analysis",
            "Other"
        ]
    )

    # Image upload
    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"],
        help="Maximum file size: 10MB"
    )

    if uploaded_file:
        # Validate size
        if uploaded_file.size > 10 * 1024 * 1024:
            st.error("❌ File too large. Maximum size: 10MB")
            return

        # Display image
        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(image, caption="Uploaded image", use_container_width=True)

        with col2:
            # Additional context
            additional_info = st.text_area(
                "Additional information (optional)",
                placeholder="e.g., Started 3 days ago, itchy, painful...",
                height=100
            )

            # Analysis settings
            show_thinking = st.checkbox("Show AI reasoning", value=False)

        # Analyze button
        if st.button("🔍 Analyze Image", type="primary", use_container_width=True):
            # Save temp file
            temp_path = Path("/tmp/uploaded_image.jpg")
            image.save(temp_path)

            # Build prompt based on check type
            prompts = {
                "Skin condition / Rash": "Analyze this skin condition photo. Describe what you observe, possible causes in postpartum context, and recommend next steps.",
                "C-section scar healing": "Assess this C-section scar for healing progress. Look for signs of proper healing or any concerns like infection, dehiscence, or keloid formation.",
                "Breast condition": "Examine this breast condition image. Look for signs of mastitis, engorgement, blocked ducts, or other breastfeeding-related issues.",
                "Baby's diaper (check for abnormalities)": "Analyze this diaper content. Check for normal vs. abnormal stool/urine patterns in newborns.",
                "Medicine verification": "Identify this medication from the pill bottle/packaging. Verify if it's commonly prescribed postpartum and note any safety concerns.",
                "Food / Meal analysis": "Analyze this meal. Assess nutritional value for postpartum recovery and breastfeeding. Suggest improvements.",
                "Other": "Analyze this image in the context of postpartum health and provide relevant insights."
            }

            prompt = prompts.get(check_type, prompts["Other"])
            if additional_info:
                prompt += f"\n\nAdditional context: {additional_info}"

            with st.spinner("Analyzing image..."):
                try:
                    if show_thinking:
                        result = gemma_client.generate_with_thinking(
                            system_prompt="You are a compassionate postpartum health AI assistant with medical knowledge.",
                            user_prompt=f"Image analysis request: {prompt}"
                        )

                        st.markdown("### 🧠 AI Reasoning Process")
                        with st.expander("How Ira analyzed this", expanded=False):
                            st.write(result["thinking"])

                        st.markdown("### 📋 Assessment")
                        st.write(result["answer"])

                    else:
                        # Use image analysis
                        response = gemma_client.generate_with_image(
                            image_path=str(temp_path),
                            prompt=prompt,
                            system_prompt="You are Ira, a compassionate postpartum health AI assistant.",
                            max_new_tokens=512
                        )

                        st.markdown("### 📋 Assessment")
                        st.write(response)

                    # Warning footer
                    st.warning(
                        "⚠️ **Important**: This is a preliminary AI assessment. "
                        "Please consult your healthcare provider for proper diagnosis and treatment. "
                        "If you notice concerning symptoms, seek medical attention immediately."
                    )

                    # Option to share with doctor
                    st.markdown("---")
                    if st.button("📤 Export Assessment"):
                        # Generate export text
                        export_text = f"""
Visual Health Check Report
Generated: {st.session_state.get('timestamp', 'Now')}

Patient: {user_profile.get('name')}
Days Postpartum: {user_profile.get('postpartum_days')}
Check Type: {check_type}

Additional Info: {additional_info or 'None provided'}

AI Assessment:
{response if not show_thinking else result['answer']}

---
Note: This is an AI-generated preliminary assessment. Professional medical evaluation is required.
"""
                        st.download_button(
                            "📥 Download Report",
                            data=export_text,
                            file_name=f"visual_check_{check_type.replace(' ', '_')}.txt",
                            mime="text/plain"
                        )

                except Exception as e:
                    st.error(f"❌ Analysis failed: {str(e)}")
                    st.warning("Please try again or consult your healthcare provider directly.")

    # Educational section
    st.markdown("---")
    with st.expander("ℹ️ What can Visual Health Check help with?"):
        st.markdown("""
**This feature can provide preliminary insights for:**

✅ **Skin conditions**: Rashes, spots, discoloration
✅ **Wound healing**: C-section or perineal tear recovery
✅ **Breast health**: Engorgement, redness, lumps
✅ **Baby monitoring**: Diaper contents, skin conditions
✅ **Medication verification**: Pill identification
✅ **Nutrition**: Meal analysis and suggestions

**Limitations:**
- AI cannot diagnose medical conditions
- Cannot prescribe medications
- Cannot replace physical examination
- May not detect subtle abnormalities

**When to see a doctor immediately:**
- Severe pain or discomfort
- Signs of infection (fever, pus, severe redness)
- Heavy bleeding or unusual discharge
- Any concerning changes in baby's health
""")
