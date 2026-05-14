"""Translation dictionaries for multi-language UI support."""

TRANSLATIONS = {
    "English": {
        # Navigation
        "nav_wellness": "Wellness Check",
        "nav_visual": "📸 Visual Health Check",
        "nav_nutrition": "Nutrition",
        "nav_tracker": "Track Your Health",
        "nav_chat": "Share with Ira",
        "nav_journal": "My Journal",
        "nav_insights": "🔍 Health Insights",
        "nav_community": "Mom's Circle",
        "nav_articles": "Articles",

        # Welcome page
        "welcome_title": "🤱 Welcome to Postpartum Care Companion",
        "welcome_subtitle": "Your Personal Postpartum Support System",
        "welcome_intro": "This AI-powered app provides safe, evidence-based support for postpartum mothers. Let's start by getting to know you better so we can personalize your experience.",
        "tell_us": "Tell us about yourself",

        # Form fields
        "your_name": "Your name (or nickname) *",
        "your_age": "Your age *",
        "days_since_delivery": "Days since delivery *",
        "number_of_children": "Number of children *",
        "current_status": "Current status *",
        "preferred_language": "Preferred language *",
        "optional_info": "Optional Information",
        "delivery_type": "Type of delivery",
        "feeding_method": "Feeding method",

        # Buttons
        "continue_to_app": "Continue to App",
        "update_profile": "📝 Update Profile",
        "get_guidance": "Get Guidance",
        "get_diet_plan": "Get Diet Plan",
        "save_entry": "Save Entry",
        "save_all_readings": "💾 Save All Readings",
        "post_tip": "Post Tip",
        "post_reply": "Post Reply",
        "clear_conversation": "🗑️ Clear conversation",

        # Common
        "language": "Language",
        "symptoms": "Symptoms",
        "notes": "Notes",
        "date": "Date",
        "days_postpartum": "Days postpartum",

        # Main page
        "welcome_back": "🤱 Welcome back",
        "tagline": "AI-powered safe support for postpartum mothers",

        # Wellness Check
        "symptom_checker": "🩺 Symptom Checker",
        "hi_message": "👋 Hi {name}! You are on day **{days}** of your postpartum journey.",
        "describe_symptoms": "Describe your symptoms",
        "show_ai_reasoning": "💭 Show AI reasoning",
        "show_ai_reasoning_help": "See how Ira analyzes your symptoms",
        "analyzing": "Analysing...",
        "please_describe_symptoms": "Please describe your symptoms.",
        "how_ira_analyzed": "### 🧠 How Ira Analyzed Your Symptoms",
        "view_ai_reasoning": "View AI reasoning process",
        "triage_guidance": "## 🧾 Triage Guidance",
        "could_not_generate_guidance": "Could not generate triage guidance. Please try again or consult your healthcare provider.",
        "diet_recommendations": "🥗 Diet Recommendations",
        "pipeline_trace": "Pipeline trace",
        "error_occurred": "❌ An error occurred during analysis: {error}",
        "please_try_again": "Please try again. If the problem persists, consult your healthcare provider directly.",

        # Nutrition
        "diet_suggestions": "🥗 Diet Suggestions",
        "nutrition_message": "👋 Hi {name}! Based on your recovery stage, we recommend **{phase}** nutrition.",
        "postpartum_phase": "Postpartum phase",
        "symptoms_optional": "Symptoms (optional)",
        "preparing_diet_plan": "Preparing personalized diet plan...",
        "your_diet_plan": "### 🥗 Your Personalized Diet Plan",
        "health_guidance": "🩺 Health Guidance",
        "could_not_generate_diet": "Could not generate diet plan. Please try again.",

        # Journal
        "journal_title": "📔 Journal",
        "journal_caption": "Write how you feel. Your entries are private.",
        "get_ai_analysis": "Get AI emotional analysis",
        "please_write_something": "Please write something before saving.",
        "analyzing_entry": "Analyzing your entry...",
        "emotional_analysis": "### 💭 Emotional Analysis",
        "entry_saved": "✅ Entry saved!",
        "your_entries": "### Your Entries",
        "view_analysis": "View emotional analysis",
        "ppd_warning": "💙 If you're experiencing persistent low mood, anxiety, or difficulty bonding with your baby, please reach out to your healthcare provider. You're not alone, and support is available.",

        # Community
        "community_tips": "💬 Community Tips",
        "community_caption": "Share your postpartum tips and experiences with other mothers.",
        "share_tip": "✍️ Share a tip",
        "your_tip": "Your tip or experience",
        "tip_posted": "✅ Tip posted!",
        "reply_posted": "Reply posted!",
        "please_write_tip": "Please write something before posting.",
        "could_not_post": "❌ Could not post tip: {error}",
        "no_tips_yet": "No tips yet. Be the first to share!",
        "reply": "Reply",
        "your_reply": "Your reply",

        # Articles
        "trusted_articles": "📰 Trusted Articles",
        "live_feeds": "### Live Feeds",
        "clinical_references": "### Clinical References",

        # Health Tracker
        "health_tracker": "📈 Health Tracker",
        "tracker_caption": "Log your daily health readings to monitor your recovery.",
        "tab_bp_sugar": "🩸 BP & Sugar",
        "tab_vitals": "🌡️ Vitals",
        "tab_sleep": "🌙 Sleep",
        "tab_cycle": "🌸 Cycle",
        "tab_pregnancy": "🤰 Pregnancy",
        "tab_history": "📊 History",

        # BP & Sugar
        "blood_pressure": "#### 🩸 Blood Pressure",
        "systolic": "Systolic (upper) mmHg",
        "diastolic": "Diastolic (lower) mmHg",
        "blood_sugar": "#### 🍬 Blood Sugar",
        "sugar_normal": "Normal (mg/dL)",
        "sugar_fasting": "Fasting (mg/dL)",
        "sugar_pp": "Postprandial (mg/dL)",

        # Vitals
        "temperature": "Temperature (°C)",
        "heart_rate": "Heart Rate (bpm)",
        "blood_oxygen": "Blood Oxygen SpO2 (%)",
        "weight": "Weight (kg)",
        "thyroid_tsh": "Thyroid TSH (mIU/L)",
        "hydration": "Water intake (glasses)",
        "mood_today": "Mood today",

        # Sleep
        "sleep_duration": "Sleep duration (hours)",
        "sleep_quality": "Sleep quality",
        "sleep_stages": "Sleep stages (if known)",

        # Cycle
        "period_log": "#### 🌸 Period Log",
        "period_status": "Period status today",
        "flow_intensity": "Flow intensity",
        "discharge_section": "#### 🌿 Discharge",
        "discharge_type": "Discharge type",
        "fertile_days": "#### 🌼 Fertile Days",
        "fertile_day": "Marking as fertile day",
        "ovulation": "Possible ovulation today",

        # Pregnancy
        "pregnancy_log": "#### 🤰 Pregnancy Log",
        "pregnancy_week": "Pregnancy week (if applicable)",
        "pregnancy_symptoms": "Symptoms today",
        "pregnancy_weight": "Weight today (kg)",
        "pregnancy_notes": "Pregnancy notes",

        # Tracker messages
        "saving_readings": "Saving your health readings...",
        "invalid_values": "❌ Invalid values detected:",
        "correct_values": "Please correct the values and try again.",
        "health_alerts": "⚠️ Health alerts detected:",
        "ai_analysis": "📋 AI Analysis",
        "readings_saved": "✅ Readings saved!",
        "all_good": "✅ All readings saved! Everything looks good.",
        "no_entries": "No entries yet. Start logging your health readings.",
        "general_notes": "General notes (optional)",

        # Chat page
        "share_with_ira": "💬 Share with Ira",
        "chat_caption": "Talk to Ira about anything — health, baby, home, or just how you feel.",
        "ira_greeting": "Namaste 🌸 {name}! I'm Ira, and I'm here for you.",
        "ira_typing": "Ira is typing...",
        "type_message": "Type your message here...",

        # Messages
        "please_enter_name": "Please enter your name",
        "please_accept_disclaimer": "Please accept the medical disclaimer to continue",
        "redirecting": "Welcome, {name}! Redirecting to your personalized dashboard...",
        "i_understand": "I Understand and Accept",
        "error_generic": "❌ An error occurred: {error}",
        "please_try_later": "Please try again later.",

        # Disclaimer
        "disclaimer_title": "⚕️ Medical Disclaimer",
        "disclaimer_text": "This app provides educational information only and is **not a substitute for professional medical advice**. Always consult your healthcare provider for medical concerns. In emergencies, call your local emergency number.",
        "disclaimer_accept": "I understand this app does not replace medical advice *",

        # Placeholders
        "placeholder_name": "e.g., Priya",
        "placeholder_symptoms": "e.g., feeling tired, breast pain, mood swings...",
        "placeholder_journal": "How are you feeling today?",
    },

    "Hindi": {
        # Navigation
        "nav_wellness": "स्वास्थ्य जांच",
        "nav_visual": "📸 दृश्य स्वास्थ्य जांच",
        "nav_nutrition": "पोषण",
        "nav_tracker": "अपना स्वास्थ्य ट्रैक करें",
        "nav_chat": "इरा से बात करें",
        "nav_journal": "मेरी डायरी",
        "nav_insights": "🔍 स्वास्थ्य जानकारी",
        "nav_community": "माँ का समुदाय",
        "nav_articles": "लेख",

        # Welcome page
        "welcome_title": "🤱 प्रसवोत्तर देखभाल साथी में आपका स्वागत है",
        "welcome_subtitle": "आपकी व्यक्तिगत प्रसवोत्तर सहायता प्रणाली",
        "welcome_intro": "यह AI-संचालित ऐप प्रसवोत्तर माताओं के लिए सुरक्षित, साक्ष्य-आधारित सहायता प्रदान करता है। आइए आपको बेहतर तरीके से जानने से शुरुआत करें ताकि हम आपके अनुभव को व्यक्तिगत बना सकें।",
        "tell_us": "हमें अपने बारे में बताएं",

        # Form fields
        "your_name": "आपका नाम (या उपनाम) *",
        "your_age": "आपकी उम्र *",
        "days_since_delivery": "प्रसव के बाद के दिन *",
        "number_of_children": "बच्चों की संख्या *",
        "current_status": "वर्तमान स्थिति *",
        "preferred_language": "पसंदीदा भाषा *",
        "optional_info": "वैकल्पिक जानकारी",
        "delivery_type": "प्रसव का प्रकार",
        "feeding_method": "स्तनपान विधि",

        # Buttons
        "continue_to_app": "ऐप पर जारी रखें",
        "update_profile": "📝 प्रोफ़ाइल अपडेट करें",
        "get_guidance": "मार्गदर्शन प्राप्त करें",
        "get_diet_plan": "आहार योजना प्राप्त करें",
        "save_entry": "प्रविष्टि सहेजें",
        "save_all_readings": "💾 सभी रीडिंग सहेजें",
        "post_tip": "सुझाव पोस्ट करें",
        "post_reply": "उत्तर पोस्ट करें",
        "clear_conversation": "🗑️ बातचीत साफ़ करें",

        # Common
        "language": "भाषा",
        "symptoms": "लक्षण",
        "notes": "नोट्स",
        "date": "तारीख",

        # Disclaimer
        "disclaimer_title": "⚕️ चिकित्सा अस्वीकरण",
        "disclaimer_text": "यह ऐप केवल शैक्षिक जानकारी प्रदान करता है और **पेशेवर चिकित्सा सलाह का विकल्प नहीं है**। चिकित्सा संबंधी चिंताओं के लिए हमेशा अपने स्वास्थ्य सेवा प्रदाता से परामर्श करें। आपातकाल में, अपना स्थानीय आपातकालीन नंबर डायल करें।",
        "disclaimer_accept": "मैं समझती हूं कि यह ऐप चिकित्सा सलाह की जगह नहीं लेता *",

        # Common
        "language": "भाषा",
        "symptoms": "लक्षण",
        "notes": "नोट्स",
        "date": "तारीख",
        "days_postpartum": "प्रसव के बाद के दिन",

        # Main page
        "welcome_back": "🤱 वापस स्वागत है",
        "tagline": "AI-संचालित सुरक्षित प्रसवोत्तर माताओं के लिए समर्थन",

        # Wellness Check
        "symptom_checker": "🩺 लक्षण जांचकर्ता",
        "hi_message": "👋 नमस्ते {name}! आप अपनी प्रसवोत्तर यात्रा के **{days}** दिन पर हैं।",
        "show_ai_reasoning": "💭 AI तर्क दिखाएं",
        "show_ai_reasoning_help": "देखें कि इरा आपके लक्षणों का विश्लेषण कैसे करती है",
        "analyzing": "विश्लेषण कर रहे हैं...",
        "please_describe_symptoms": "कृपया अपने लक्षणों का वर्णन करें।",
        "how_ira_analyzed": "### 🧠 इरा ने आपके लक्षणों का विश्लेषण कैसे किया",
        "view_ai_reasoning": "AI तर्क प्रक्रिया देखें",
        "triage_guidance": "## 🧾 ट्राइएज मार्गदर्शन",
        "could_not_generate_guidance": "ट्राइएज मार्गदर्शन उत्पन्न नहीं कर सके। कृपया पुनः प्रयास करें या अपने स्वास्थ्य सेवा प्रदाता से परामर्श करें।",
        "diet_recommendations": "🥗 आहार सिफारिशें",
        "pipeline_trace": "पाइपलाइन ट्रेस",
        "error_occurred": "❌ विश्लेषण के दौरान एक त्रुटि हुई: {error}",
        "please_try_again": "कृपया पुनः प्रयास करें। यदि समस्या बनी रहती है, तो सीधे अपने स्वास्थ्य सेवा प्रदाता से परामर्श करें।",

        # Nutrition
        "diet_suggestions": "🥗 आहार सुझाव",
        "nutrition_message": "👋 नमस्ते {name}! आपकी रिकवरी के चरण के आधार पर, हम **{phase}** पोषण की सिफारिश करते हैं।",
        "postpartum_phase": "प्रसवोत्तर चरण",
        "symptoms_optional": "लक्षण (वैकल्पिक)",
        "preparing_diet_plan": "व्यक्तिगत आहार योजना तैयार कर रहे हैं...",
        "your_diet_plan": "### 🥗 आपकी व्यक्तिगत आहार योजना",
        "health_guidance": "🩺 स्वास्थ्य मार्गदर्शन",
        "could_not_generate_diet": "आहार योजना उत्पन्न नहीं कर सके। कृपया पुनः प्रयास करें।",

        # Journal
        "journal_title": "📔 जर्नल",
        "journal_caption": "लिखें कि आप कैसा महसूस कर रही हैं। आपकी प्रविष्टियाँ निजी हैं।",
        "get_ai_analysis": "AI भावनात्मक विश्लेषण प्राप्त करें",
        "please_write_something": "सहेजने से पहले कृपया कुछ लिखें।",
        "analyzing_entry": "आपकी प्रविष्टि का विश्लेषण कर रहे हैं...",
        "emotional_analysis": "### 💭 भावनात्मक विश्लेषण",
        "entry_saved": "✅ प्रविष्टि सहेजी गई!",
        "your_entries": "### आपकी प्रविष्टियाँ",
        "view_analysis": "भावनात्मक विश्लेषण देखें",
        "ppd_warning": "💙 यदि आप लगातार कम मनोदशा, चिंता, या अपने बच्चे के साथ बंधन में कठिनाई का अनुभव कर रही हैं, तो कृपया अपने स्वास्थ्य सेवा प्रदाता से संपर्क करें। आप अकेली नहीं हैं, और सहायता उपलब्ध है।",

        # Community
        "community_tips": "💬 समुदाय सुझाव",
        "community_caption": "अन्य माताओं के साथ अपने प्रसवोत्तर सुझाव और अनुभव साझा करें।",
        "share_tip": "✍️ एक सुझाव साझा करें",
        "your_tip": "आपका सुझाव या अनुभव",
        "tip_posted": "✅ सुझाव पोस्ट किया गया!",
        "reply_posted": "उत्तर पोस्ट किया गया!",
        "please_write_tip": "पोस्ट करने से पहले कृपया कुछ लिखें।",
        "could_not_post": "❌ सुझाव पोस्ट नहीं कर सके: {error}",
        "no_tips_yet": "अभी तक कोई सुझाव नहीं। साझा करने वाली पहली बनें!",
        "reply": "उत्तर दें",
        "your_reply": "आपका उत्तर",

        # Articles
        "trusted_articles": "📰 विश्वसनीय लेख",
        "live_feeds": "### लाइव फ़ीड",
        "clinical_references": "### नैदानिक संदर्भ",

        # Health Tracker
        "health_tracker": "📈 स्वास्थ्य ट्रैकर",
        "tracker_caption": "अपनी रिकवरी की निगरानी के लिए अपनी दैनिक स्वास्थ्य रीडिंग लॉग करें।",
        "tab_bp_sugar": "🩸 BP और शुगर",
        "tab_vitals": "🌡️ वाइटल्स",
        "tab_sleep": "🌙 नींद",
        "tab_cycle": "🌸 साइकिल",
        "tab_pregnancy": "🤰 गर्भावस्था",
        "tab_history": "📊 इतिहास",

        # BP & Sugar
        "blood_pressure": "#### 🩸 रक्तचाप",
        "systolic": "सिस्टोलिक (ऊपरी) mmHg",
        "diastolic": "डायस्टोलिक (निचला) mmHg",
        "blood_sugar": "#### 🍬 रक्त शर्करा",
        "sugar_normal": "सामान्य (mg/dL)",
        "sugar_fasting": "उपवास (mg/dL)",
        "sugar_pp": "भोजन के बाद (mg/dL)",

        # Vitals
        "temperature": "तापमान (°C)",
        "heart_rate": "हृदय गति (bpm)",
        "blood_oxygen": "रक्त ऑक्सीजन SpO2 (%)",
        "weight": "वजन (kg)",
        "thyroid_tsh": "थायरॉइड TSH (mIU/L)",
        "hydration": "पानी का सेवन (गिलास)",
        "mood_today": "आज का मूड",

        # Sleep
        "sleep_duration": "नींद की अवधि (घंटे)",
        "sleep_quality": "नींद की गुणवत्ता",
        "sleep_stages": "नींद के चरण (यदि ज्ञात हो)",

        # Cycle
        "period_log": "#### 🌸 पीरियड लॉग",
        "period_status": "आज पीरियड की स्थिति",
        "flow_intensity": "फ्लो की तीव्रता",
        "discharge_section": "#### 🌿 डिस्चार्ज",
        "discharge_type": "डिस्चार्ज का प्रकार",
        "fertile_days": "#### 🌼 उपजाऊ दिन",
        "fertile_day": "उपजाऊ दिन के रूप में चिह्नित करना",
        "ovulation": "आज संभावित ओव्यूलेशन",

        # Pregnancy
        "pregnancy_log": "#### 🤰 गर्भावस्था लॉग",
        "pregnancy_week": "गर्भावस्था सप्ताह (यदि लागू हो)",
        "pregnancy_symptoms": "आज के लक्षण",
        "pregnancy_weight": "आज का वजन (kg)",
        "pregnancy_notes": "गर्भावस्था नोट्स",

        # Tracker messages
        "saving_readings": "आपकी स्वास्थ्य रीडिंग सहेज रहे हैं...",
        "invalid_values": "❌ अमान्य मान पाए गए:",
        "correct_values": "कृपया मानों को सही करें और पुनः प्रयास करें।",
        "health_alerts": "⚠️ स्वास्थ्य चेतावनियां पाई गईं:",
        "ai_analysis": "📋 AI विश्लेषण",
        "readings_saved": "✅ रीडिंग सहेजी गईं!",
        "all_good": "✅ सभी रीडिंग सहेजी गईं! सब कुछ अच्छा लग रहा है।",
        "no_entries": "अभी तक कोई प्रविष्टि नहीं। अपनी स्वास्थ्य रीडिंग लॉग करना शुरू करें।",
        "general_notes": "सामान्य नोट्स (वैकल्पिक)",

        # Chat page
        "share_with_ira": "💬 इरा से साझा करें",
        "chat_caption": "इरा से किसी भी चीज़ के बारे में बात करें — स्वास्थ्य, बच्चा, घर, या बस आप कैसा महसूस करती हैं।",
        "ira_greeting": "नमस्ते 🌸 {name}! मैं इरा हूं, और मैं आपके लिए यहां हूं।",
        "ira_typing": "इरा टाइप कर रही है...",
        "type_message": "यहाँ अपना संदेश टाइप करें...",

        # Messages
        "please_enter_name": "कृपया अपना नाम दर्ज करें",
        "please_accept_disclaimer": "जारी रखने के लिए कृपया चिकित्सा अस्वीकरण स्वीकार करें",
        "redirecting": "स्वागत है, {name}! आपके व्यक्तिगत डैशबोर्ड पर रीडायरेक्ट कर रहे हैं...",
        "i_understand": "मैं समझती हूं और स्वीकार करती हूं",
        "error_generic": "❌ एक त्रुटि हुई: {error}",
        "please_try_later": "कृपया बाद में पुनः प्रयास करें।",

        # Placeholders
        "placeholder_name": "जैसे, प्रिया",
        "placeholder_symptoms": "जैसे, थकान महसूस करना, स्तन दर्द, मूड स्विंग्स...",
        "placeholder_journal": "आज आप कैसा महसूस कर रही हैं?",
    },

    "Tamil": {
        # Navigation
        "nav_wellness": "நல்வாழ்வு சோதனை",
        "nav_visual": "📸 காட்சி சுகாதார சோதனை",
        "nav_nutrition": "ஊட்டச்சத்து",
        "nav_tracker": "உங்கள் சுகாதாரத்தை கண்காணிக்கவும்",
        "nav_chat": "இராவுடன் பகிரவும்",
        "nav_journal": "என் பதிவேடு",
        "nav_insights": "🔍 சுகாதார நுண்ணறிவுகள்",
        "nav_community": "அம்மாவின் வட்டம்",
        "nav_articles": "கட்டுரைகள்",

        # Welcome page
        "welcome_title": "🤱 பிரசவத்திற்குப் பிந்தைய பராமரிப்பு துணைக்கு வரவேற்கிறோம்",
        "welcome_subtitle": "உங்கள் தனிப்பட்ட பிரசவத்திற்குப் பிந்தைய ஆதரவு அமைப்பு",
        "welcome_intro": "இந்த AI-இயக்கப்படும் பயன்பாடு பிரசவத்திற்குப் பிந்தைய தாய்மார்களுக்கு பாதுகாப்பான, ஆதார அடிப்படையிலான ஆதரவை வழங்குகிறது. உங்களை நன்றாக தெரிந்துகொள்வதன் மூலம் தொடங்குவோம்.",
        "tell_us": "உங்களைப் பற்றி எங்களுக்கு சொல்லுங்கள்",

        # Form fields
        "your_name": "உங்கள் பெயர் (அல்லது செல்லப்பெயர்) *",
        "your_age": "உங்கள் வயது *",
        "days_since_delivery": "பிரசவத்திற்குப் பிறகு நாட்கள் *",
        "number_of_children": "குழந்தைகளின் எண்ணிக்கை *",
        "current_status": "தற்போதைய நிலை *",
        "preferred_language": "விருப்ப மொழி *",
        "optional_info": "விருப்பத் தகவல்",
        "delivery_type": "பிரசவ வகை",
        "feeding_method": "உணவூட்டும் முறை",

        # Buttons
        "continue_to_app": "பயன்பாட்டைத் தொடரவும்",
        "update_profile": "📝 சுயவிவரத்தைப் புதுப்பிக்கவும்",
        "get_guidance": "வழிகாட்டுதலைப் பெறவும்",
        "get_diet_plan": "உணவுத் திட்டத்தைப் பெறவும்",
        "save_entry": "பதிவைச் சேமிக்கவும்",
        "save_all_readings": "💾 அனைத்து வாசிப்புகளையும் சேமிக்கவும்",
        "post_tip": "குறிப்பை இடுகையிடவும்",
        "post_reply": "பதிலை இடுகையிடவும்",
        "clear_conversation": "🗑️ உரையாடலை அழிக்கவும்",

        # Common
        "language": "மொழி",
        "symptoms": "அறிகுறிகள்",
        "notes": "குறிப்புகள்",
        "date": "தேதி",

        # Disclaimer
        "disclaimer_title": "⚕️ மருத்துவ மறுப்பு",
        "disclaimer_text": "இந்த பயன்பாடு கல்வித் தகவலை மட்டுமே வழங்குகிறது மற்றும் **தொழில்முறை மருத்துவ ஆலோசனைக்கு மாற்றாக இல்லை**. மருத்துவ கவலைகளுக்கு எப்போதும் உங்கள் சுகாதார வழங்குநரை அணுகவும். அவசரநிலைகளில், உங்கள் உள்ளூர் அவசர எண்ணை அழைக்கவும்.",
        "disclaimer_accept": "இந்த பயன்பாடு மருத்துவ ஆலோசனையை மாற்றாது என்பதை நான் புரிந்துகொள்கிறேன் *",

        # Common
        "language": "மொழி",
        "symptoms": "அறிகுறிகள்",
        "notes": "குறிப்புகள்",
        "date": "தேதி",
        "days_postpartum": "பிரசவத்திற்குப் பிந்தைய நாட்கள்",

        # Main page
        "welcome_back": "🤱 மீண்டும் வரவேற்கிறோம்",
        "tagline": "AI-இயக்கப்படும் பாதுகாப்பான பிரசவத்திற்குப் பிந்தைய தாய்மார்களுக்கான ஆதரவு",

        # Wellness/Nutrition/Journal/Community/Articles/Tracker/Chat - abbreviated Tamil keys
        "symptom_checker": "🩺 அறிகுறி சோதனையாளர்",
        "hi_message": "👋 வணக்கம் {name}! நீங்கள் உங்கள் பிரசவத்திற்குப் பிந்தைய பயணத்தின் **{days}** நாளில் இருக்கிறீர்கள்.",
        "show_ai_reasoning": "💭 AI பகுத்தறிவைக் காட்டு",
        "analyzing": "பகுப்பாய்வு செய்கிறது...",
        "diet_suggestions": "🥗 உணவு பரிந்துரைகள்",
        "journal_title": "📔 பதிவேடு",
        "community_tips": "💬 சமூக குறிப்புகள்",
        "trusted_articles": "📰 நம்பகமான கட்டுரைகள்",
        "health_tracker": "📈 சுகாதார கண்காணிப்பு",
        "share_with_ira": "💬 இராவுடன் பகிரவும்",

        # Placeholders
        "placeholder_name": "எ.கா., பிரியா",
        "placeholder_symptoms": "எ.கா., சோர்வு, மார்பக வலி, மனநிலை மாற்றங்கள்...",
        "placeholder_journal": "இன்று நீங்கள் எப்படி உணர்கிறீர்கள்?",
    },

    "Telugu": {
        # Navigation
        "nav_wellness": "ఆరోగ్య తనిఖీ",
        "nav_visual": "📸 దృశ్య ఆరోగ్య తనిఖీ",
        "nav_nutrition": "పోషకాహారం",
        "nav_tracker": "మీ ఆరోగ్యాన్ని ట్రాక్ చేయండి",
        "nav_chat": "ఇరాతో భాగస్వామ్యం చేయండి",
        "nav_journal": "నా జర్నల్",
        "nav_insights": "🔍 ఆరోగ్య అంతర్దృష్టులు",
        "nav_community": "తల్లుల వృత్తం",
        "nav_articles": "వ్యాసాలు",

        # Welcome page
        "welcome_title": "🤱 ప్రసవానంతర సంరక్షణ సహచరునికి స్వాగతం",
        "welcome_subtitle": "మీ వ్యక్తిగత ప్రసవానంతర మద్దతు వ్యవస్థ",
        "welcome_intro": "ఈ AI-శక్తితో కూడిన యాప్ ప్రసవానంతర తల్లులకు సురక్షితమైన, సాక్ష్యం-ఆధారిత మద్దతును అందిస్తుంది. మిమ్మల్ని మెరుగ్గా తెలుసుకోవడం ద్వారా ప్రారంభిద్దాం.",
        "tell_us": "మీ గురించి మాకు చెప్పండి",

        # Form fields
        "your_name": "మీ పేరు (లేదా ముద్దు పేరు) *",
        "your_age": "మీ వయస్సు *",
        "days_since_delivery": "ప్రసవం తర్వాత రోజులు *",
        "number_of_children": "పిల్లల సంఖ్య *",
        "current_status": "ప్రస్తుత స్థితి *",
        "preferred_language": "ఇష్టమైన భాష *",
        "optional_info": "ఐచ్ఛిక సమాచారం",
        "delivery_type": "ప్రసవ రకం",
        "feeding_method": "దాణా పద్ధతి",

        # Buttons
        "continue_to_app": "యాప్‌కు కొనసాగించండి",
        "update_profile": "📝 ప్రొఫైల్‌ను నవీకరించండి",
        "get_guidance": "మార్గదర్శకత్వం పొందండి",
        "get_diet_plan": "ఆహార ప్రణాళికను పొందండి",
        "save_entry": "ఎంట్రీని సేవ్ చేయండి",
        "save_all_readings": "💾 అన్ని రీడింగ్‌లను సేవ్ చేయండి",
        "post_tip": "చిట్కాను పోస్ట్ చేయండి",
        "post_reply": "ప్రత్యుత్తరం పోస్ట్ చేయండి",
        "clear_conversation": "🗑️ సంభాషణను క్లియర్ చేయండి",

        # Common
        "language": "భాష",
        "symptoms": "లక్షణాలు",
        "notes": "గమనికలు",
        "date": "తేదీ",

        # Disclaimer
        "disclaimer_title": "⚕️ వైద్య నిరాకరణ",
        "disclaimer_text": "ఈ యాప్ విద్యా సమాచారాన్ని మాత్రమే అందిస్తుంది మరియు **వృత్తిపరమైన వైద్య సలహాకు ప్రత్యామ్నాయం కాదు**. వైద్య ఆందోళనల కోసం ఎల్లప్పుడూ మీ ఆరోగ్య సంరక్షణ ప్రదాతను సంప్రదించండి. అత్యవసర పరిస్థితులలో, మీ స్థానిక అత్యవసర నంబర్‌కు కాల్ చేయండి.",
        "disclaimer_accept": "ఈ యాప్ వైద్య సలహాను భర్తీ చేయదని నేను అర్థం చేసుకున్నాను *",

        # Common
        "language": "భాష",
        "symptoms": "లక్షణాలు",
        "notes": "గమనికలు",
        "date": "తేదీ",
        "days_postpartum": "ప్రసవం తర్వాత రోజులు",

        # Main page
        "welcome_back": "🤱 తిరిగి స్వాగతం",
        "tagline": "AI-శక్తితో కూడిన సురక్షితమైన ప్రసవానంతర తల్లులకు మద్దతు",

        # Pages
        "symptom_checker": "🩺 లక్షణ తనిఖీదారు",
        "hi_message": "👋 హలో {name}! మీరు మీ ప్రసవానంతర ప్రయాణంలో **{days}** రోజులో ఉన్నారు.",
        "diet_suggestions": "🥗 ఆహార సూచనలు",
        "journal_title": "📔 జర్నల్",
        "community_tips": "💬 సంఘ చిట్కాలు",
        "health_tracker": "📈 ఆరోగ్య ట్రాకర్",
        "trusted_articles": "📰 విశ్వసనీయ వ్యాసాలు",
        "share_with_ira": "💬 ఇరాతో భాగస్వామ్యం చేయండి",

        # Placeholders
        "placeholder_name": "ఉదా., ప్రియ",
        "placeholder_symptoms": "ఉదా., అలసట, రొమ్ము నొప్పి, మానసిక మార్పులు...",
        "placeholder_journal": "ఈరోజు మీరు ఎలా అనుభూతి చెందుతున్నారు?",
    },

    "Bengali": {
        # Navigation
        "nav_wellness": "সুস্থতা পরীক্ষা",
        "nav_visual": "📸 ভিজ্যুয়াল স্বাস্থ্য পরীক্ষা",
        "nav_nutrition": "পুষ্টি",
        "nav_tracker": "আপনার স্বাস্থ্য ট্র্যাক করুন",
        "nav_chat": "ইরার সাথে শেয়ার করুন",
        "nav_journal": "আমার জার্নাল",
        "nav_insights": "🔍 স্বাস্থ্য অন্তর্দৃষ্টি",
        "nav_community": "মায়ের বৃত্ত",
        "nav_articles": "নিবন্ধ",

        # Welcome page
        "welcome_title": "🤱 প্রসবোত্তর যত্ন সঙ্গীতে স্বাগতম",
        "welcome_subtitle": "আপনার ব্যক্তিগত প্রসবোত্তর সহায়তা ব্যবস্থা",
        "welcome_intro": "এই AI-চালিত অ্যাপ প্রসবোত্তর মায়েদের জন্য নিরাপদ, প্রমাণ-ভিত্তিক সহায়তা প্রদান করে। আপনাকে আরও ভালভাবে জানার মাধ্যমে শুরু করি।",
        "tell_us": "আপনার সম্পর্কে আমাদের বলুন",

        # Form fields
        "your_name": "আপনার নাম (বা ডাকনাম) *",
        "your_age": "আপনার বয়স *",
        "days_since_delivery": "প্রসবের পর দিন *",
        "number_of_children": "সন্তানের সংখ্যা *",
        "current_status": "বর্তমান অবস্থা *",
        "preferred_language": "পছন্দের ভাষা *",
        "optional_info": "ঐচ্ছিক তথ্য",
        "delivery_type": "প্রসবের ধরন",
        "feeding_method": "খাওয়ানোর পদ্ধতি",

        # Buttons
        "continue_to_app": "অ্যাপে চালিয়ে যান",
        "update_profile": "📝 প্রোফাইল আপডেট করুন",
        "get_guidance": "নির্দেশনা পান",
        "get_diet_plan": "ডায়েট প্ল্যান পান",
        "save_entry": "এন্ট্রি সংরক্ষণ করুন",
        "save_all_readings": "💾 সব রিডিং সংরক্ষণ করুন",
        "post_tip": "টিপ পোস্ট করুন",
        "post_reply": "উত্তর পোস্ট করুন",
        "clear_conversation": "🗑️ কথোপকথন পরিষ্কার করুন",

        # Common
        "language": "ভাষা",
        "symptoms": "লক্ষণ",
        "notes": "নোট",
        "date": "তারিখ",
        "days_postpartum": "প্রসবের পর দিন",

        # Main page
        "welcome_back": "🤱 ফিরে স্বাগতম",
        "tagline": "AI-চালিত নিরাপদ প্রসবোত্তর মায়েদের জন্য সহায়তা",

        # Pages
        "symptom_checker": "🩺 লক্ষণ পরীক্ষক",
        "hi_message": "👋 হ্যালো {name}! আপনি আপনার প্রসবোত্তর যাত্রার **{days}** দিনে আছেন।",
        "diet_suggestions": "🥗 ডায়েট পরামর্শ",
        "journal_title": "📔 জার্নাল",
        "community_tips": "💬 কমিউনিটি টিপস",
        "health_tracker": "📈 স্বাস্থ্য ট্র্যাকার",
        "trusted_articles": "📰 বিশ্বস্ত নিবন্ধ",
        "share_with_ira": "💬 ইরার সাথে শেয়ার করুন",

        # Disclaimer
        "disclaimer_title": "⚕️ চিকিৎসা দাবিত্যাগ",
        "disclaimer_text": "এই অ্যাপটি শুধুমাত্র শিক্ষামূলক তথ্য প্রদান করে এবং **পেশাদার চিকিৎসা পরামর্শের বিকল্প নয়**। চিকিৎসা সংক্রান্ত উদ্বেগের জন্য সর্বদা আপনার স্বাস্থ্যসেবা প্রদানকারীর সাথে পরামর্শ করুন। জরুরি অবস্থায়, আপনার স্থানীয় জরুরি নম্বরে কল করুন।",
        "disclaimer_accept": "আমি বুঝতে পারছি যে এই অ্যাপ চিকিৎসা পরামর্শের প্রতিস্থাপন করে না *",

        # Placeholders
        "placeholder_name": "যেমন, প্রিয়া",
        "placeholder_symptoms": "যেমন, ক্লান্তি, স্তন ব্যথা, মেজাজ পরিবর্তন...",
        "placeholder_journal": "আজ আপনি কেমন অনুভব করছেন?",
    },

    "Marathi": {
        # Navigation
        "nav_wellness": "आरोग्य तपासणी",
        "nav_visual": "📸 व्हिज्युअल आरोग्य तपासणी",
        "nav_nutrition": "पोषण",
        "nav_tracker": "तुमचे आरोग्य ट्रॅक करा",
        "nav_chat": "इरासोबत शेअर करा",
        "nav_journal": "माझे जर्नल",
        "nav_insights": "🔍 आरोग्य माहिती",
        "nav_community": "आईचे वर्तुळ",
        "nav_articles": "लेख",

        # Welcome page
        "welcome_title": "🤱 प्रसवोत्तर काळजी साथीदारात आपले स्वागत आहे",
        "welcome_subtitle": "तुमची वैयक्तिक प्रसवोत्तर समर्थन प्रणाली",
        "welcome_intro": "हे AI-चालित अॅप प्रसवोत्तर मातांसाठी सुरक्षित, पुराव्यावर आधारित समर्थन प्रदान करते. तुम्हाला अधिक चांगल्या प्रकारे जाणून घेऊन सुरुवात करूया.",
        "tell_us": "तुमच्याबद्दल आम्हाला सांगा",

        # Form fields
        "your_name": "तुमचे नाव (किंवा टोपणनाव) *",
        "your_age": "तुमचे वय *",
        "days_since_delivery": "प्रसवानंतरचे दिवस *",
        "number_of_children": "मुलांची संख्या *",
        "current_status": "सध्याची स्थिती *",
        "preferred_language": "पसंतीची भाषा *",
        "optional_info": "पर्यायी माहिती",
        "delivery_type": "प्रसवाचा प्रकार",
        "feeding_method": "आहार देण्याची पद्धत",

        # Buttons
        "continue_to_app": "अॅपवर सुरू ठेवा",
        "update_profile": "📝 प्रोफाइल अपडेट करा",
        "get_guidance": "मार्गदर्शन मिळवा",
        "get_diet_plan": "आहार योजना मिळवा",
        "save_entry": "नोंद जतन करा",
        "save_all_readings": "💾 सर्व वाचन जतन करा",
        "post_tip": "टीप पोस्ट करा",
        "post_reply": "उत्तर पोस्ट करा",
        "clear_conversation": "🗑️ संभाषण साफ करा",

        # Common
        "language": "भाषा",
        "symptoms": "लक्षणे",
        "notes": "टिपा",
        "date": "तारीख",

        # Disclaimer
        "disclaimer_title": "⚕️ वैद्यकीय अस्वीकरण",
        "disclaimer_text": "हे अॅप केवळ शैक्षणिक माहिती प्रदान करते आणि **व्यावसायिक वैद्यकीय सल्ल्याचा पर्याय नाही**. वैद्यकीय चिंतेसाठी नेहमी तुमच्या आरोग्य सेवा प्रदात्याशी सल्लामसलत करा. आणीबाणीच्या परिस्थितीत, तुमचा स्थानिक आणीबाणी क्रमांक डायल करा.",
        "disclaimer_accept": "मला समजले आहे की हे अॅप वैद्यकीय सल्ल्याची जागा घेत नाही *",

        # Common
        "language": "भाषा",
        "symptoms": "लक्षणे",
        "notes": "टिपा",
        "date": "तारीख",
        "days_postpartum": "प्रसवानंतरचे दिवस",

        # Main/Pages
        "welcome_back": "🤱 पुन्हा स्वागत आहे",
        "symptom_checker": "🩺 लक्षण तपासणी",
        "diet_suggestions": "🥗 आहार सूचना",
        "journal_title": "📔 जर्नल",
        "community_tips": "💬 समुदाय टिपा",
        "health_tracker": "📈 आरोग्य ट्रॅकर",
        "trusted_articles": "📰 विश्वसनीय लेख",
        "share_with_ira": "💬 इरासोबत शेअर करा",

        # Placeholders
        "placeholder_name": "उदा., प्रिया",
        "placeholder_symptoms": "उदा., थकवा, स्तन वेदना, मूड बदल...",
        "placeholder_journal": "आज तुम्हाला कसे वाटते?",
    },

    "Gujarati": {
        # Navigation
        "nav_wellness": "આરોગ્ય તપાસ",
        "nav_visual": "📸 વિઝ્યુઅલ આરોગ્ય તપાસ",
        "nav_nutrition": "પોષણ",
        "nav_tracker": "તમારું આરોગ્ય ટ્રૅક કરો",
        "nav_chat": "ઇરા સાથે શેર કરો",
        "nav_journal": "મારી ડાયરી",
        "nav_insights": "🔍 આરોગ્ય માહિતી",
        "nav_community": "માતાનું વર્તુળ",
        "nav_articles": "લેખો",

        # Welcome page
        "welcome_title": "🤱 પ્રસૂતિ પછીની સંભાળ સાથીદારમાં આપનું સ્વાગત છે",
        "welcome_subtitle": "તમારી વ્યક્તિગત પ્રસૂતિ પછીની સહાય પ્રણાલી",
        "welcome_intro": "આ AI-સંચાલિત એપ્લિકેશન પ્રસૂતિ પછીની માતાઓ માટે સુરક્ષિત, પુરાવા આધારિત સહાય પ્રદાન કરે છે. ચાલો તમને વધુ સારી રીતે જાણીને શરૂઆત કરીએ.",
        "tell_us": "અમને તમારા વિશે જણાવો",

        # Form fields
        "your_name": "તમારું નામ (અથવા ઉપનામ) *",
        "your_age": "તમારી ઉંમર *",
        "days_since_delivery": "પ્રસૂતિ પછીના દિવસો *",
        "number_of_children": "બાળકોની સંખ્યા *",
        "current_status": "વર્તમાન સ્થિતિ *",
        "preferred_language": "પસંદગીની ભાષા *",
        "optional_info": "વૈકલ્પિક માહિતી",
        "delivery_type": "પ્રસૂતિનો પ્રકાર",
        "feeding_method": "ખોરાક આપવાની પદ્ધતિ",

        # Buttons
        "continue_to_app": "એપ પર ચાલુ રાખો",
        "update_profile": "📝 પ્રોફાઇલ અપડેટ કરો",
        "get_guidance": "માર્ગદર્શન મેળવો",
        "get_diet_plan": "આહાર યોજના મેળવો",
        "save_entry": "એન્ટ્રી સાચવો",
        "save_all_readings": "💾 બધા રીડિંગ્સ સાચવો",
        "post_tip": "ટિપ પોસ્ટ કરો",
        "post_reply": "જવાબ પોસ્ટ કરો",
        "clear_conversation": "🗑️ વાર્તાલાપ સાફ કરો",

        # Common
        "language": "ભાષા",
        "symptoms": "લક્ષણો",
        "notes": "નોંધો",
        "date": "તારીખ",

        # Disclaimer
        "disclaimer_title": "⚕️ તબીબી અસ્વીકરણ",
        "disclaimer_text": "આ એપ્લિકેશન ફક્ત શૈક્ષણિક માહિતી પ્રદાન કરે છે અને **વ્યાવસાયિક તબીબી સલાહનો વિકલ્પ નથી**. તબીબી ચિંતાઓ માટે હંમેશા તમારા આરોગ્ય સેવા પ્રદાતાનો સંપર્ક કરો. કટોકટીમાં, તમારો સ્થાનિક ઇમરજન્સી નંબર ડાયલ કરો.",
        "disclaimer_accept": "હું સમજું છું કે આ એપ તબીબી સલાહની જગ્યા લેતી નથી *",

        # Common
        "language": "ભાષા",
        "symptoms": "લક્ષણો",
        "notes": "નોંધો",
        "date": "તારીખ",
        "days_postpartum": "પ્રસૂતિ પછીના દિવસો",

        # Main/Pages
        "welcome_back": "🤱 પાછા સ્વાગત છે",
        "symptom_checker": "🩺 લક્ષણ તપાસનાર",
        "diet_suggestions": "🥗 આહાર સૂચનો",
        "journal_title": "📔 જર્નલ",
        "community_tips": "💬 સમુદાય ટિપ્સ",
        "health_tracker": "📈 આરોગ્ય ટ્રૅકર",
        "trusted_articles": "📰 વિશ્વસનીય લેખો",
        "share_with_ira": "💬 ઇરા સાથે શેર કરો",

        # Placeholders
        "placeholder_name": "દા.ત., પ્રિયા",
        "placeholder_symptoms": "દા.ત., થાક, સ્તન દુખાવો, મૂડ ફેરફારો...",
        "placeholder_journal": "આજે તમે કેવું અનુભવો છો?",
    },

    "Kannada": {
        "nav_wellness": "ಆರೋಗ್ಯ ಪರೀಕ್ಷೆ",
        "nav_visual": "📸 ದೃಶ್ಯ ಆರೋಗ್ಯ ಪರೀಕ್ಷೆ",
        "nav_nutrition": "ಪೋಷಣೆ",
        "nav_tracker": "ನಿಮ್ಮ ಆರೋಗ್ಯವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ",
        "nav_chat": "ಇರಾ ಜೊತೆ ಹಂಚಿಕೊಳ್ಳಿ",
        "nav_journal": "ನನ್ನ ಜರ್ನಲ್",
        "nav_insights": "🔍 ಆರೋಗ್ಯ ಒಳನೋಟಗಳು",
        "nav_community": "ತಾಯಿಯ ವಲಯ",
        "nav_articles": "ಲೇಖನಗಳು",
        "welcome_title": "🤱 ಪ್ರಸವಾನಂತರದ ಆರೈಕೆ ಸಹಚರರಿಗೆ ಸ್ವಾಗತ",
        "welcome_subtitle": "ನಿಮ್ಮ ವೈಯಕ್ತಿಕ ಪ್ರಸವಾನಂತರದ ಬೆಂಬಲ ವ್ಯವಸ್ಥೆ",
        "welcome_intro": "ಈ AI-ಚಾಲಿತ ಅಪ್ಲಿಕೇಶನ್ ಪ್ರಸವಾನಂತರದ ತಾಯಂದಿರಿಗೆ ಸುರಕ್ಷಿತ, ಸಾಕ್ಷ್ಯ-ಆಧಾರಿತ ಬೆಂಬಲವನ್ನು ಒದಗಿಸುತ್ತದೆ.",
        "tell_us": "ನಿಮ್ಮ ಬಗ್ಗೆ ನಮಗೆ ತಿಳಿಸಿ",
        "your_name": "ನಿಮ್ಮ ಹೆಸರು *",
        "your_age": "ನಿಮ್ಮ ವಯಸ್ಸು *",
        "days_since_delivery": "ಪ್ರಸವದ ನಂತರದ ದಿನಗಳು *",
        "number_of_children": "ಮಕ್ಕಳ ಸಂಖ್ಯೆ *",
        "current_status": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ *",
        "preferred_language": "ಆದ್ಯತೆಯ ಭಾಷೆ *",
        "optional_info": "ಐಚ್ಛಿಕ ಮಾಹಿತಿ",
        "delivery_type": "ಪ್ರಸವದ ಪ್ರಕಾರ",
        "feeding_method": "ಆಹಾರ ವಿಧಾನ",
        "continue_to_app": "ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಮುಂದುವರಿಸಿ",
        "update_profile": "📝 ಪ್ರೊಫೈಲ್ ನವೀಕರಿಸಿ",
        "get_guidance": "ಮಾರ್ಗದರ್ಶನ ಪಡೆಯಿರಿ",
        "get_diet_plan": "ಆಹಾರ ಯೋಜನೆ ಪಡೆಯಿರಿ",
        "save_entry": "ನಮೂದು ಉಳಿಸಿ",
        "save_all_readings": "💾 ಎಲ್ಲಾ ವಾಚನಗಳನ್ನು ಉಳಿಸಿ",
        "post_tip": "ಸಲಹೆ ಪೋಸ್ಟ್ ಮಾಡಿ",
        "post_reply": "ಪ್ರತ್ಯುತ್ತರ ಪೋಸ್ಟ್ ಮಾಡಿ",
        "clear_conversation": "🗑️ ಸಂಭಾಷಣೆ ತೆರವುಗೊಳಿಸಿ",
        "language": "ಭಾಷೆ",
        "symptoms": "ಲಕ್ಷಣಗಳು",
        "notes": "ಟಿಪ್ಪಣಿಗಳು",
        "date": "ದಿನಾಂಕ",
        "days_postpartum": "ಪ್ರಸವದ ನಂತರದ ದಿನಗಳು",

        # Main/Pages
        "welcome_back": "🤱 ಮತ್ತೆ ಸ್ವಾಗತ",
        "symptom_checker": "🩺 ಲಕ್ಷಣ ಪರೀಕ್ಷಕ",
        "diet_suggestions": "🥗 ಆಹಾರ ಸಲಹೆಗಳು",
        "journal_title": "📔 ಜರ್ನಲ್",
        "community_tips": "💬 ಸಮುದಾಯ ಸಲಹೆಗಳು",
        "health_tracker": "📈 ಆರೋಗ್ಯ ಟ್ರ್ಯಾಕರ್",
        "trusted_articles": "📰 ವಿಶ್ವಾಸಾರ್ಹ ಲೇಖನಗಳು",
        "share_with_ira": "💬 ಇರಾ ಜೊತೆ ಹಂಚಿಕೊಳ್ಳಿ",

        "disclaimer_title": "⚕️ ವೈದ್ಯಕೀಯ ನಿರಾಕರಣೆ",
        "disclaimer_text": "ಈ ಅಪ್ಲಿಕೇಶನ್ ಕೇವಲ ಶೈಕ್ಷಣಿಕ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸುತ್ತದೆ ಮತ್ತು **ವೃತ್ತಿಪರ ವೈದ್ಯಕೀಯ ಸಲಹೆಗೆ ಪರ್ಯಾಯವಲ್ಲ**.",
        "disclaimer_accept": "ಈ ಅಪ್ಲಿಕೇಶನ್ ವೈದ್ಯಕೀಯ ಸಲಹೆಯನ್ನು ಬದಲಿಸುವುದಿಲ್ಲ ಎಂದು ನಾನು ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇನೆ *",
        "placeholder_name": "ಉದಾ., ಪ್ರಿಯಾ",
        "placeholder_symptoms": "ಉದಾ., ಆಯಾಸ, ಸ್ತನ ನೋವು...",
        "placeholder_journal": "ಇಂದು ನೀವು ಹೇಗೆ ಭಾವಿಸುತ್ತೀರಿ?",
    },

    "Malayalam": {
        "nav_wellness": "ആരോഗ്യ പരിശോധന",
        "nav_visual": "📸 ദൃശ്യ ആരോഗ്യ പരിശോധന",
        "nav_nutrition": "പോഷകാഹാരം",
        "nav_tracker": "നിങ്ങളുടെ ആരോഗ്യം ട്രാക്ക് ചെയ്യുക",
        "nav_chat": "ഇറയുമായി പങ്കിടുക",
        "nav_journal": "എന്റെ ജേർണൽ",
        "nav_insights": "🔍 ആരോഗ്യ സൂചനകൾ",
        "nav_community": "അമ്മമാരുടെ വൃത്തം",
        "nav_articles": "ലേഖനങ്ങൾ",
        "welcome_title": "🤱 പ്രസവാനന്തര പരിചരണ കൂട്ടുകാരനിലേക്ക് സ്വാഗതം",
        "welcome_subtitle": "നിങ്ങളുടെ വ്യക്തിഗത പ്രസവാനന്തര പിന്തുണ സംവിധാനം",
        "welcome_intro": "ഈ AI-പവർഡ് ആപ്പ് പ്രസവാനന്തര അമ്മമാർക്ക് സുരക്ഷിതവും തെളിവ് അടിസ്ഥാനമാക്കിയുള്ളതുമായ പിന്തുണ നൽകുന്നു.",
        "tell_us": "നിങ്ങളെക്കുറിച്ച് പറയുക",
        "your_name": "നിങ്ങളുടെ പേര് *",
        "your_age": "നിങ്ങളുടെ പ്രായം *",
        "days_since_delivery": "പ്രസവശേഷമുള്ള ദിവസങ്ങൾ *",
        "number_of_children": "കുട്ടികളുടെ എണ്ണം *",
        "current_status": "നിലവിലെ സ്ഥിതി *",
        "preferred_language": "ഇഷ്ടപ്പെട്ട ഭാഷ *",
        "optional_info": "ഓപ്ഷണൽ വിവരങ്ങൾ",
        "delivery_type": "പ്രസവ തരം",
        "feeding_method": "ഭക്ഷണം നൽകൽ രീതി",
        "continue_to_app": "ആപ്പിലേക്ക് തുടരുക",
        "update_profile": "📝 പ്രൊഫൈൽ അപ്ഡേറ്റ് ചെയ്യുക",
        "get_guidance": "മാർഗ്ഗനിർദ്ദേശം നേടുക",
        "get_diet_plan": "ഭക്ഷണ പദ്ധതി നേടുക",
        "save_entry": "എൻട്രി സേവ് ചെയ്യുക",
        "save_all_readings": "💾 എല്ലാ റീഡിംഗുകളും സേവ് ചെയ്യുക",
        "post_tip": "ടിപ്പ് പോസ്റ്റ് ചെയ്യുക",
        "post_reply": "മറുപടി പോസ്റ്റ് ചെയ്യുക",
        "clear_conversation": "🗑️ സംഭാഷണം മായ്ക്കുക",
        "language": "ഭാഷ",
        "symptoms": "ലക്ഷണങ്ങൾ",
        "notes": "കുറിപ്പുകൾ",
        "date": "തീയതി",
        "days_postpartum": "പ്രസവശേഷമുള്ള ദിവസങ്ങൾ",

        # Main/Pages
        "welcome_back": "🤱 തിരിച്ചു സ്വാഗതം",
        "symptom_checker": "🩺 ലക്ഷണ പരിശോധകൻ",
        "diet_suggestions": "🥗 ഭക്ഷണ നിർദ്ദേശങ്ങൾ",
        "journal_title": "📔 ജേർണൽ",
        "community_tips": "💬 കമ്മ്യൂണിറ്റി ടിപ്പുകൾ",
        "health_tracker": "📈 ആരോഗ്യ ട്രാക്കർ",
        "trusted_articles": "📰 വിശ്വസനീയ ലേഖനങ്ങൾ",
        "share_with_ira": "💬 ഇറയുമായി പങ്കിടുക",

        "disclaimer_title": "⚕️ മെഡിക്കൽ നിരാകരണം",
        "disclaimer_text": "ഈ ആപ്പ് വിദ്യാഭ്യാസ വിവരങ്ങൾ മാത്രം നൽകുന്നു, **പ്രൊഫഷണൽ മെഡിക്കൽ ഉപദേശത്തിന് പകരമല്ല**.",
        "disclaimer_accept": "ഈ ആപ്പ് മെഡിക്കൽ ഉപദേശത്തിന് പകരമാകില്ലെന്ന് ഞാൻ മനസ്സിലാക്കുന്നു *",
        "placeholder_name": "ഉദാ., പ്രിയ",
        "placeholder_symptoms": "ഉദാ., ക്ഷീണം, സ്തന വേദന...",
        "placeholder_journal": "ഇന്ന് നിങ്ങൾക്ക് എങ്ങനെ തോന്നുന്നു?",
    },

    "Punjabi": {
        "nav_wellness": "ਸਿਹਤ ਜਾਂਚ",
        "nav_visual": "📸 ਵਿਜ਼ੂਅਲ ਸਿਹਤ ਜਾਂਚ",
        "nav_nutrition": "ਪੋਸ਼ਣ",
        "nav_tracker": "ਆਪਣੀ ਸਿਹਤ ਟਰੈਕ ਕਰੋ",
        "nav_chat": "ਇਰਾ ਨਾਲ ਸਾਂਝਾ ਕਰੋ",
        "nav_journal": "ਮੇਰੀ ਡਾਇਰੀ",
        "nav_insights": "🔍 ਸਿਹਤ ਜਾਣਕਾਰੀ",
        "nav_community": "ਮਾਂ ਦਾ ਸਰਕਲ",
        "nav_articles": "ਲੇਖ",
        "welcome_title": "🤱 ਜਣੇਪੇ ਬਾਅਦ ਦੇਖਭਾਲ ਸਾਥੀ ਵਿੱਚ ਸੁਆਗਤ ਹੈ",
        "welcome_subtitle": "ਤੁਹਾਡਾ ਨਿੱਜੀ ਜਣੇਪੇ ਬਾਅਦ ਸਹਾਇਤਾ ਪ੍ਰਣਾਲੀ",
        "welcome_intro": "ਇਹ AI-ਸੰਚਾਲਿਤ ਐਪ ਜਣੇਪੇ ਬਾਅਦ ਮਾਵਾਂ ਲਈ ਸੁਰੱਖਿਅਤ, ਸਬੂਤ-ਆਧਾਰਿਤ ਸਹਾਇਤਾ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ।",
        "tell_us": "ਸਾਨੂੰ ਆਪਣੇ ਬਾਰੇ ਦੱਸੋ",
        "your_name": "ਤੁਹਾਡਾ ਨਾਮ *",
        "your_age": "ਤੁਹਾਡੀ ਉਮਰ *",
        "days_since_delivery": "ਜਣੇਪੇ ਤੋਂ ਬਾਅਦ ਦੇ ਦਿਨ *",
        "number_of_children": "ਬੱਚਿਆਂ ਦੀ ਗਿਣਤੀ *",
        "current_status": "ਮੌਜੂਦਾ ਸਥਿਤੀ *",
        "preferred_language": "ਪਸੰਦੀਦਾ ਭਾਸ਼ਾ *",
        "optional_info": "ਵਿਕਲਪਿਕ ਜਾਣਕਾਰੀ",
        "delivery_type": "ਜਣੇਪੇ ਦੀ ਕਿਸਮ",
        "feeding_method": "ਖੁਰਾਕ ਦੇਣ ਦਾ ਤਰੀਕਾ",
        "continue_to_app": "ਐਪ ਤੇ ਜਾਰੀ ਰੱਖੋ",
        "update_profile": "📝 ਪ੍ਰੋਫਾਈਲ ਅੱਪਡੇਟ ਕਰੋ",
        "get_guidance": "ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਾਪਤ ਕਰੋ",
        "get_diet_plan": "ਖੁਰਾਕ ਯੋਜਨਾ ਪ੍ਰਾਪਤ ਕਰੋ",
        "save_entry": "ਐਂਟਰੀ ਸੇਵ ਕਰੋ",
        "save_all_readings": "💾 ਸਾਰੀਆਂ ਰੀਡਿੰਗਾਂ ਸੇਵ ਕਰੋ",
        "post_tip": "ਸੁਝਾਅ ਪੋਸਟ ਕਰੋ",
        "post_reply": "ਜਵਾਬ ਪੋਸਟ ਕਰੋ",
        "clear_conversation": "🗑️ ਗੱਲਬਾਤ ਸਾਫ਼ ਕਰੋ",
        "language": "ਭਾਸ਼ਾ",
        "symptoms": "ਲੱਛਣ",
        "notes": "ਨੋਟਸ",
        "date": "ਤਾਰੀਖ",
        "days_postpartum": "ਜਣੇਪੇ ਤੋਂ ਬਾਅਦ ਦੇ ਦਿਨ",

        # Main/Pages
        "welcome_back": "🤱 ਮੁੜ ਸੁਆਗਤ ਹੈ",
        "symptom_checker": "🩺 ਲੱਛਣ ਜਾਂਚਕਰਤਾ",
        "diet_suggestions": "🥗 ਖੁਰਾਕ ਸੁਝਾਅ",
        "journal_title": "📔 ਜਰਨਲ",
        "community_tips": "💬 ਕਮਿਊਨਿਟੀ ਟਿਪਸ",
        "health_tracker": "📈 ਸਿਹਤ ਟਰੈਕਰ",
        "trusted_articles": "📰 ਭਰੋਸੇਮੰਦ ਲੇਖ",
        "share_with_ira": "💬 ਇਰਾ ਨਾਲ ਸਾਂਝਾ ਕਰੋ",

        "disclaimer_title": "⚕️ ਮੈਡੀਕਲ ਅਸਵੀਕਰਨ",
        "disclaimer_text": "ਇਹ ਐਪ ਸਿਰਫ਼ ਸਿੱਖਿਆ ਸੰਬੰਧੀ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ ਅਤੇ **ਪੇਸ਼ੇਵਰ ਮੈਡੀਕਲ ਸਲਾਹ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ**।",
        "disclaimer_accept": "ਮੈਂ ਸਮਝਦੀ ਹਾਂ ਕਿ ਇਹ ਐਪ ਮੈਡੀਕਲ ਸਲਾਹ ਦੀ ਥਾਂ ਨਹੀਂ ਲੈਂਦੀ *",
        "placeholder_name": "ਜਿਵੇਂ, ਪ੍ਰਿਯਾ",
        "placeholder_symptoms": "ਜਿਵੇਂ, ਥਕਾਵਟ, ਛਾਤੀ ਦਰਦ...",
        "placeholder_journal": "ਅੱਜ ਤੁਸੀਂ ਕਿਵੇਂ ਮਹਿਸੂਸ ਕਰ ਰਹੇ ਹੋ?",
    },

    "Urdu": {
        "nav_wellness": "صحت کی جانچ",
        "nav_visual": "📸 بصری صحت کی جانچ",
        "nav_nutrition": "غذائیت",
        "nav_tracker": "اپنی صحت کو ٹریک کریں",
        "nav_chat": "ایرا کے ساتھ شیئر کریں",
        "nav_journal": "میری ڈائری",
        "nav_insights": "🔍 صحت کی معلومات",
        "nav_community": "ماں کا حلقہ",
        "nav_articles": "مضامین",
        "welcome_title": "🤱 پیدائش کے بعد کی دیکھ بھال کے ساتھی میں خوش آمدید",
        "welcome_subtitle": "آپ کا ذاتی پیدائش کے بعد کی مدد کا نظام",
        "welcome_intro": "یہ AI سے چلنے والی ایپ پیدائش کے بعد کی ماؤں کے لیے محفوظ، ثبوت پر مبنی مدد فراہم کرتی ہے۔",
        "tell_us": "ہمیں اپنے بارے میں بتائیں",
        "your_name": "آپ کا نام *",
        "your_age": "آپ کی عمر *",
        "days_since_delivery": "پیدائش کے بعد کے دن *",
        "number_of_children": "بچوں کی تعداد *",
        "current_status": "موجودہ حیثیت *",
        "preferred_language": "پسندیدہ زبان *",
        "optional_info": "اختیاری معلومات",
        "delivery_type": "پیدائش کی قسم",
        "feeding_method": "کھانا کھلانے کا طریقہ",
        "continue_to_app": "ایپ پر جاری رکھیں",
        "update_profile": "📝 پروفائل اپ ڈیٹ کریں",
        "get_guidance": "رہنمائی حاصل کریں",
        "get_diet_plan": "خوراک کا منصوبہ حاصل کریں",
        "save_entry": "اندراج محفوظ کریں",
        "save_all_readings": "💾 تمام ریڈنگز محفوظ کریں",
        "post_tip": "تجویز پوسٹ کریں",
        "post_reply": "جواب پوسٹ کریں",
        "clear_conversation": "🗑️ گفتگو صاف کریں",
        "language": "زبان",
        "symptoms": "علامات",
        "notes": "نوٹس",
        "date": "تاریخ",
        "days_postpartum": "پیدائش کے بعد کے دن",

        # Main/Pages
        "welcome_back": "🤱 واپسی مبارک",
        "symptom_checker": "🩺 علامات جانچنے والا",
        "diet_suggestions": "🥗 خوراک تجاویز",
        "journal_title": "📔 ڈائری",
        "community_tips": "💬 کمیونٹی تجاویز",
        "health_tracker": "📈 صحت ٹریکر",
        "trusted_articles": "📰 قابل اعتماد مضامین",
        "share_with_ira": "💬 ایرا کے ساتھ شیئر کریں",

        "disclaimer_title": "⚕️ طبی اعلان دستبرداری",
        "disclaimer_text": "یہ ایپ صرف تعلیمی معلومات فراہم کرتی ہے اور **پیشہ ورانہ طبی مشورے کا متبادل نہیں ہے**۔",
        "disclaimer_accept": "میں سمجھتی ہوں کہ یہ ایپ طبی مشورے کی جگہ نہیں لیتی *",
        "placeholder_name": "مثال، پریا",
        "placeholder_symptoms": "مثال، تھکاوٹ، چھاتی میں درد...",
        "placeholder_journal": "آج آپ کیسا محسوس کر رہی ہیں؟",
    },

    "Odia": {
        "nav_wellness": "ସ୍ୱାସ୍ଥ୍ୟ ଯାଞ୍ଚ",
        "nav_visual": "📸 ଭିଜୁଆଲ୍ ସ୍ୱାସ୍ଥ୍ୟ ଯାଞ୍ଚ",
        "nav_nutrition": "ପୋଷଣ",
        "nav_tracker": "ଆପଣଙ୍କ ସ୍ୱାସ୍ଥ୍ୟ ଟ୍ରାକ୍ କରନ୍ତୁ",
        "nav_chat": "ଇରା ସହିତ ଶେୟାର୍ କରନ୍ତୁ",
        "nav_journal": "ମୋର ଜର୍ନାଲ୍",
        "nav_insights": "🔍 ସ୍ୱାସ୍ଥ୍ୟ ସୂଚନା",
        "nav_community": "ମା'ର ବୃତ୍ତ",
        "nav_articles": "ପ୍ରବନ୍ଧ",
        "welcome_title": "🤱 ପ୍ରସବ ପରବର୍ତ୍ତୀ ଯତ୍ନ ସାଥୀକୁ ସ୍ୱାଗତ",
        "welcome_subtitle": "ଆପଣଙ୍କର ବ୍ୟକ୍ତିଗତ ପ୍ରସବ ପରବର୍ତ୍ତୀ ସହାୟତା ବ୍ୟବସ୍ଥା",
        "welcome_intro": "ଏହି AI-ଚାଳିତ ଆପ୍ ପ୍ରସବ ପରବର୍ତ୍ତୀ ମାତାମାନଙ୍କ ପାଇଁ ସୁରକ୍ଷିତ, ପ୍ରମାଣ-ଆଧାରିତ ସହାୟତା ପ୍ରଦାନ କରେ।",
        "tell_us": "ଆମକୁ ଆପଣଙ୍କ ବିଷୟରେ କୁହନ୍ତୁ",
        "your_name": "ଆପଣଙ୍କ ନାମ *",
        "your_age": "ଆପଣଙ୍କ ବୟସ *",
        "days_since_delivery": "ପ୍ରସବ ପରେ ଦିନ *",
        "number_of_children": "ପିଲାମାନଙ୍କ ସଂଖ୍ୟା *",
        "current_status": "ବର୍ତ୍ତମାନ ସ୍ଥିତି *",
        "preferred_language": "ପସନ୍ଦର ଭାଷା *",
        "optional_info": "ଇଚ୍ଛାଧୀନ ସୂଚନା",
        "delivery_type": "ପ୍ରସବ ପ୍ରକାର",
        "feeding_method": "ଖାଦ୍ୟ ଦେବାର ପଦ୍ଧତି",
        "continue_to_app": "ଆପ୍‌କୁ ଜାରି ରଖନ୍ତୁ",
        "update_profile": "📝 ପ୍ରୋଫାଇଲ୍ ଅପଡେଟ୍ କରନ୍ତୁ",
        "get_guidance": "ମାର୍ଗଦର୍ଶନ ପାଆନ୍ତୁ",
        "get_diet_plan": "ଖାଦ୍ୟ ଯୋଜନା ପାଆନ୍ତୁ",
        "save_entry": "ଏଣ୍ଟ୍ରି ସେଭ୍ କରନ୍ତୁ",
        "save_all_readings": "💾 ସମସ୍ତ ରିଡିଂ ସେଭ୍ କରନ୍ତୁ",
        "post_tip": "ଟିପ୍ ପୋଷ୍ଟ କରନ୍ତୁ",
        "post_reply": "ଉତ୍ତର ପୋଷ୍ଟ କରନ୍ତୁ",
        "clear_conversation": "🗑️ ବାର୍ତ୍ତାଳାପ ସଫା କରନ୍ତୁ",
        "language": "ଭାଷା",
        "symptoms": "ଲକ୍ଷଣ",
        "notes": "ନୋଟ୍ସ",
        "date": "ତାରିଖ",
        "days_postpartum": "ପ୍ରସବ ପରେ ଦିନ",

        # Main/Pages
        "welcome_back": "🤱 ପୁଣି ସ୍ୱାଗତ",
        "symptom_checker": "🩺 ଲକ୍ଷଣ ପରୀକ୍ଷକ",
        "diet_suggestions": "🥗 ଖାଦ୍ୟ ପରାମର୍ଶ",
        "journal_title": "📔 ଜର୍ନାଲ୍",
        "community_tips": "💬 ସମୁଦାୟ ଟିପ୍ସ",
        "health_tracker": "📈 ସ୍ୱାସ୍ଥ୍ୟ ଟ୍ରାକର୍",
        "trusted_articles": "📰 ବିଶ୍ୱସ୍ତ ପ୍ରବନ୍ଧ",
        "share_with_ira": "💬 ଇରା ସହିତ ଶେୟାର୍ କରନ୍ତୁ",

        "disclaimer_title": "⚕️ ଚିକିତ୍ସା ଅସ୍ୱୀକରଣ",
        "disclaimer_text": "ଏହି ଆପ୍ କେବଳ ଶିକ୍ଷାଗତ ସୂଚନା ପ୍ରଦାନ କରେ ଏବଂ **ବୃତ୍ତିଗତ ଚିକିତ୍ସା ପରାମର୍ଶର ବିକଳ୍ପ ନୁହେଁ**।",
        "disclaimer_accept": "ମୁଁ ବୁଝୁଛି ଯେ ଏହି ଆପ୍ ଚିକିତ୍ସା ପରାମର୍ଶକୁ ବଦଳାଏ ନାହିଁ *",
        "placeholder_name": "ଯେମିତି, ପ୍ରିୟା",
        "placeholder_symptoms": "ଯେମିତି, କ୍ଲାନ୍ତି, ସ୍ତନ ଯନ୍ତ୍ରଣା...",
        "placeholder_journal": "ଆଜି ଆପଣ କିପରି ଅନୁଭବ କରୁଛନ୍ତି?",
    },

    "Nepali": {
        "nav_wellness": "स्वास्थ्य जाँच",
        "nav_visual": "📸 दृश्य स्वास्थ्य जाँच",
        "nav_nutrition": "पोषण",
        "nav_tracker": "आफ्नो स्वास्थ्य ट्र्याक गर्नुहोस्",
        "nav_chat": "इरासँग साझा गर्नुहोस्",
        "nav_journal": "मेरो जर्नल",
        "nav_insights": "🔍 स्वास्थ्य जानकारी",
        "nav_community": "आमाको सर्कल",
        "nav_articles": "लेखहरू",
        "welcome_title": "🤱 प्रसवोत्तर हेरचाह साथीमा स्वागत छ",
        "welcome_subtitle": "तपाईंको व्यक्तिगत प्रसवोत्तर समर्थन प्रणाली",
        "welcome_intro": "यो AI-संचालित एप प्रसवोत्तर आमाहरूका लागि सुरक्षित, प्रमाण-आधारित समर्थन प्रदान गर्दछ।",
        "tell_us": "हामीलाई तपाईंको बारेमा बताउनुहोस्",
        "your_name": "तपाईंको नाम *",
        "your_age": "तपाईंको उमेर *",
        "days_since_delivery": "प्रसव पछिका दिनहरू *",
        "number_of_children": "बच्चाहरूको संख्या *",
        "current_status": "वर्तमान स्थिति *",
        "preferred_language": "रुचाइएको भाषा *",
        "optional_info": "वैकल्पिक जानकारी",
        "delivery_type": "प्रसवको प्रकार",
        "feeding_method": "खुवाउने विधि",
        "continue_to_app": "एपमा जारी राख्नुहोस्",
        "update_profile": "📝 प्रोफाइल अपडेट गर्नुहोस्",
        "get_guidance": "मार्गदर्शन प्राप्त गर्नुहोस्",
        "get_diet_plan": "आहार योजना प्राप्त गर्नुहोस्",
        "save_entry": "प्रविष्टि सुरक्षित गर्नुहोस्",
        "save_all_readings": "💾 सबै रिडिङहरू सुरक्षित गर्नुहोस्",
        "post_tip": "सुझाव पोस्ट गर्नुहोस्",
        "post_reply": "जवाफ पोस्ट गर्नुहोस्",
        "clear_conversation": "🗑️ वार्तालाप खाली गर्नुहोस्",
        "language": "भाषा",
        "symptoms": "लक्षणहरू",
        "notes": "टिप्पणीहरू",
        "date": "मिति",
        "days_postpartum": "प्रसव पछिका दिनहरू",

        # Main/Pages
        "welcome_back": "🤱 फेरि स्वागत छ",
        "symptom_checker": "🩺 लक्षण जाँचकर्ता",
        "diet_suggestions": "🥗 आहार सुझावहरू",
        "journal_title": "📔 जर्नल",
        "community_tips": "💬 समुदाय सुझावहरू",
        "health_tracker": "📈 स्वास्थ्य ट्र्याकर",
        "trusted_articles": "📰 विश्वसनीय लेखहरू",
        "share_with_ira": "💬 इरासँग साझा गर्नुहोस्",

        "disclaimer_title": "⚕️ चिकित्सा अस्वीकरण",
        "disclaimer_text": "यो एप केवल शैक्षिक जानकारी प्रदान गर्दछ र **व्यावसायिक चिकित्सा सल्लाहको विकल्प होइन**।",
        "disclaimer_accept": "म बुझ्छु कि यो एपले चिकित्सा सल्लाहको ठाउँ लिँदैन *",
        "placeholder_name": "जस्तै, प्रिया",
        "placeholder_symptoms": "जस्तै, थकान, स्तन दुखाइ...",
        "placeholder_journal": "आज तपाईं कस्तो महसुस गर्दै हुनुहुन्छ?",
    },

    "Assamese": {
        "nav_wellness": "স্বাস্থ্য পৰীক্ষা",
        "nav_visual": "📸 ভিজুৱেল স্বাস্থ্য পৰীক্ষা",
        "nav_nutrition": "পুষ্টি",
        "nav_tracker": "আপোনাৰ স্বাস্থ্য ট্ৰেক কৰক",
        "nav_chat": "ইৰাৰ সৈতে শ্বেয়াৰ কৰক",
        "nav_journal": "মোৰ জাৰ্নেল",
        "nav_insights": "🔍 স্বাস্থ্য অন্তৰ্দৃষ্টি",
        "nav_community": "মাকৰ বৃত্ত",
        "nav_articles": "প্ৰবন্ধসমূহ",
        "welcome_title": "🤱 প্ৰসৱোত্তৰ যত্ন সংগীলৈ স্বাগতম",
        "welcome_subtitle": "আপোনাৰ ব্যক্তিগত প্ৰসৱোত্তৰ সহায় ব্যৱস্থা",
        "welcome_intro": "এই AI-চালিত এপে প্ৰসৱোত্তৰ মাতৃসকলৰ বাবে সুৰক্ষিত, প্ৰমাণ-ভিত্তিক সহায় প্ৰদান কৰে।",
        "tell_us": "আমাক আপোনাৰ বিষয়ে কওক",
        "your_name": "আপোনাৰ নাম *",
        "your_age": "আপোনাৰ বয়স *",
        "days_since_delivery": "প্ৰসৱৰ পিছৰ দিনবোৰ *",
        "number_of_children": "সন্তানৰ সংখ্যা *",
        "current_status": "বৰ্তমান স্থিতি *",
        "preferred_language": "পছন্দৰ ভাষা *",
        "optional_info": "ঐচ্ছিক তথ্য",
        "delivery_type": "প্ৰসৱৰ প্ৰকাৰ",
        "feeding_method": "খুৱাবলৈ পদ্ধতি",
        "continue_to_app": "এপত অব্যাহত ৰাখক",
        "update_profile": "📝 প্ৰ'ফাইল আপডেট কৰক",
        "get_guidance": "নিৰ্দেশনা লাভ কৰক",
        "get_diet_plan": "আহাৰ পৰিকল্পনা লাভ কৰক",
        "save_entry": "এণ্ট্ৰি সংৰক্ষণ কৰক",
        "save_all_readings": "💾 সকলো ৰিডিং সংৰক্ষণ কৰক",
        "post_tip": "টিপ পোষ্ট কৰক",
        "post_reply": "উত্তৰ পোষ্ট কৰক",
        "clear_conversation": "🗑️ কথোপকথন পৰিষ্কাৰ কৰক",
        "language": "ভাষা",
        "symptoms": "লক্ষণসমূহ",
        "notes": "টোকাসমূহ",
        "date": "তাৰিখ",
        "days_postpartum": "প্ৰসৱৰ পিছৰ দিনবোৰ",

        # Main/Pages
        "welcome_back": "🤱 পুনৰ স্বাগতম",
        "symptom_checker": "🩺 লক্ষণ পৰীক্ষক",
        "diet_suggestions": "🥗 আহাৰ পৰামৰ্শ",
        "journal_title": "📔 জাৰ্নেল",
        "community_tips": "💬 সমুদায় টিপছ",
        "health_tracker": "📈 স্বাস্থ্য ট্ৰেকাৰ",
        "trusted_articles": "📰 বিশ্বাসযোগ্য প্ৰবন্ধ",
        "share_with_ira": "💬 ইৰাৰ সৈতে শ্বেয়াৰ কৰক",

        "disclaimer_title": "⚕️ চিকিৎসা দাবীত্যাগ",
        "disclaimer_text": "এই এপে কেৱল শিক্ষামূলক তথ্য প্ৰদান কৰে আৰু **পেছাদাৰী চিকিৎসা পৰামৰ্শৰ বিকল্প নহয়**।",
        "disclaimer_accept": "মই বুজি পাইছো যে এই এপে চিকিৎসা পৰামৰ্শ সলনি নকৰে *",
        "placeholder_name": "যেনে, প্ৰিয়া",
        "placeholder_symptoms": "যেনে, ভাগৰ, স্তনৰ বিষ...",
        "placeholder_journal": "আজি আপুনি কেনে অনুভৱ কৰিছে?",
    },

    "Hinglish": {
        "nav_wellness": "Wellness Check",
        "nav_visual": "📸 Visual Health Check",
        "nav_nutrition": "Nutrition",
        "nav_tracker": "Apni Health Track Karein",
        "nav_chat": "Ira se Baat Karein",
        "nav_journal": "Meri Diary",
        "nav_insights": "🔍 Health Insights",
        "nav_community": "Mom's Circle",
        "nav_articles": "Articles",
        "welcome_title": "🤱 Postpartum Care Companion mein Aapka Swagat Hai",
        "welcome_subtitle": "Aapki Personal Postpartum Support System",
        "welcome_intro": "Yeh AI-powered app postpartum mothers ke liye safe, evidence-based support provide karta hai. Chaliye aapko better jaankar shuru karte hain.",
        "tell_us": "Apne baare mein bataiye",
        "your_name": "Aapka naam (ya nickname) *",
        "your_age": "Aapki umar *",
        "days_since_delivery": "Delivery ke baad ke din *",
        "number_of_children": "Bachon ki sankhya *",
        "current_status": "Current status *",
        "preferred_language": "Pasandida bhasha *",
        "optional_info": "Optional Information",
        "delivery_type": "Delivery ka type",
        "feeding_method": "Feeding method",
        "continue_to_app": "App pe Continue Karein",
        "update_profile": "📝 Profile Update Karein",
        "get_guidance": "Guidance Prapt Karein",
        "get_diet_plan": "Diet Plan Prapt Karein",
        "save_entry": "Entry Save Karein",
        "save_all_readings": "💾 Sabhi Readings Save Karein",
        "post_tip": "Tip Post Karein",
        "post_reply": "Reply Post Karein",
        "clear_conversation": "🗑️ Conversation Clear Karein",
        "language": "Bhasha",
        "symptoms": "Symptoms",
        "notes": "Notes",
        "date": "Tarikh",
        "days_postpartum": "Delivery ke baad ke din",

        # Main/Pages
        "welcome_back": "🤱 Wapas Swagat Hai",
        "symptom_checker": "🩺 Symptom Checker",
        "diet_suggestions": "🥗 Diet Suggestions",
        "journal_title": "📔 Journal",
        "community_tips": "💬 Community Tips",
        "health_tracker": "📈 Health Tracker",
        "trusted_articles": "📰 Trusted Articles",
        "share_with_ira": "💬 Ira se Share Karein",

        "disclaimer_title": "⚕️ Medical Disclaimer",
        "disclaimer_text": "Yeh app sirf educational information provide karta hai aur **professional medical advice ka replacement nahi hai**. Medical concerns ke liye hamesha apne healthcare provider se consult karein. Emergency mein, apna local emergency number dial karein.",
        "disclaimer_accept": "Main samajhti hoon ki yeh app medical advice ki jagah nahi leta *",
        "placeholder_name": "jaise, Priya",
        "placeholder_symptoms": "jaise, thakan, breast pain, mood swings...",
        "placeholder_journal": "Aaj aap kaisa feel kar rahi hain?",
    },
}

def t(key: str, lang: str = "English") -> str:
    """
    Translation helper function.
    Returns translated text for given key and language.
    Falls back to English if translation not found.
    """
    if lang in TRANSLATIONS and key in TRANSLATIONS[lang]:
        return TRANSLATIONS[lang][key]
    elif key in TRANSLATIONS["English"]:
        return TRANSLATIONS["English"][key]
    else:
        return key  # Return key itself if not found
