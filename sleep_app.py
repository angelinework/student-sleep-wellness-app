import streamlit as st

# PAGE CONFIG
st.set_page_config(page_title="Student Sleep Health Analyzer", page_icon="🌙")

# SIMPLE COLOR STYLE
st.markdown("""
<style>
body {
    background-color: #F7F9FC;
}
h1, h2, h3 {
    color: #2C6E91;
}
</style>
""", unsafe_allow_html=True)


# Language selection
language = st.selectbox("Select Language / ഭാഷ തിരഞ്ഞെടുക്കുക", ["English", "Malayalam"])

# Text dictionary
text = {

"English": {

"title": "Student Sleep Health Analyzer",

"desc": """
A simple digital wellness tool designed to help students understand how
sleep, phone usage, and travel fatigue affect stress and academic focus.
""",

"name": "Enter your name",

"sleep": "How many hours do you sleep per night?",

"phone": "Night phone usage (hours)",

"travel": "Daily school travel time (minutes)",

"analyze": "Analyze Sleep Health",

"results": "Results",

"stress": "Stress Level",

"score": "Stress Score",

"plan": "Weekly Recovery Plan",

"habits": "Habit Tracker",

"caption": "Educational sleep awareness tool for students.",

"excellent": "Sleep Health: Excellent",

"fair": "Sleep Health: Fair",

"risk": "Sleep Health: At Risk",

"highrisk": "Sleep Health: High Risk",

"recommend": "Recommended tonight: sleep",

"great": "Great! Your sleep meets the recommended level.",

"phonewarn": "Late-night phone use may be affecting sleep.",

"travelwarn": "Long travel time may require earlier bedtime.",

"focuswarn": "Low sleep may affect memory and study focus.",

"habit1": "Sleep before 11 PM",

"habit2": "Avoid phone 1 hour before sleep",

"habit3": "Morning sunlight",

"habit4": "Exercise 20 minutes",

"habit5": "No caffeine after evening",

"completed": "Habits completed",

"champ": "🏆 Sleep Champion",

"good": "⭐ Good Progress",

"keep": "⚡ Keep Building Healthy Habits",

"start": "Start building healthy sleep habits today"

},

"Malayalam": {

"title": "വിദ്യാർത്ഥികളുടെ ഉറക്ക ആരോഗ്യ വിശകലന ഉപകരണം",

"desc": """
ഉറക്കം, ഫോൺ ഉപയോഗം, യാത്ര ക്ഷീണം എന്നിവ വിദ്യാർത്ഥികളുടെ
സമ്മർദ്ദത്തെയും പഠന ശ്രദ്ധയെയും എങ്ങനെ ബാധിക്കുന്നു എന്ന് മനസ്സിലാക്കാൻ
സഹായിക്കുന്ന ഒരു ഡിജിറ്റൽ ഉപകരണം.
""",

"name": "പേര് നൽകുക",

"sleep": "ഒരു രാത്രിയിൽ എത്ര മണിക്കൂർ ഉറങ്ങുന്നു?",

"phone": "രാത്രിയിലെ ഫോൺ ഉപയോഗം (മണിക്കൂർ)",

"travel": "സ്കൂളിലേക്കുള്ള യാത്ര സമയം (മിനിറ്റ്)",

"analyze": "ഉറക്ക ആരോഗ്യ വിശകലനം",

"results": "ഫലം",

"stress": "സമ്മർദ്ദ നില",

"score": "സമ്മർദ്ദ സ്കോർ",

"plan": "വാരാന്ത്യ മെച്ചപ്പെടുത്തൽ പദ്ധതി",

"habits": "ആരോഗ്യ ശീലങ്ങൾ",

"caption": "വിദ്യാർത്ഥികൾക്കുള്ള ഉറക്ക ബോധവൽക്കരണ ഉപകരണം.",

"excellent": "ഉറക്ക ആരോഗ്യം: വളരെ നല്ലത്",

"fair": "ഉറക്ക ആരോഗ്യം: ശരാശരി",

"risk": "ഉറക്ക ആരോഗ്യം: ശ്രദ്ധ ആവശ്യം",

"highrisk": "ഉറക്ക ആരോഗ്യം: ഉയർന്ന അപകടസാധ്യത",

"recommend": "ഇന്ന് രാത്രി കൂടുതൽ ഉറങ്ങാൻ ശ്രമിക്കുക:",

"great": "നന്നായി! നിങ്ങളുടെ ഉറക്കം ശുപാർശ ചെയ്ത നിലവാരത്തിലാണ്.",

"phonewarn": "രാത്രിയിൽ ഫോൺ ഉപയോഗം ഉറക്കത്തെ ബാധിക്കാം.",

"travelwarn": "ദീർഘമായ യാത്ര സമയത്തിന് മുമ്പേ ഉറങ്ങേണ്ടിവരും.",

"focuswarn": "കുറഞ്ഞ ഉറക്കം പഠനത്തിൽ ശ്രദ്ധ കുറയ്ക്കാം.",

"habit1": "11 മണിക്ക് മുമ്പ് ഉറങ്ങുക",

"habit2": "ഉറങ്ങാൻ 1 മണിക്കൂർ മുമ്പ് ഫോൺ ഒഴിവാക്കുക",

"habit3": "പ്രഭാത സൂര്യപ്രകാശം",

"habit4": "20 മിനിറ്റ് വ്യായാമം",

"habit5": "വൈകുന്നേരത്തിന് ശേഷം കഫെയ്ൻ ഒഴിവാക്കുക",

"completed": "പൂർത്തിയാക്കിയ ശീലങ്ങൾ",

"champ": "🏆 ഉറക്ക ചാമ്പ്യൻ",

"good": "⭐ നല്ല പുരോഗതി",

"keep": "⚡ ആരോഗ്യ ശീലങ്ങൾ തുടരുക",

"start": "ആരോഗ്യകരമായ ഉറക്ക ശീലങ്ങൾ തുടങ്ങുക"

}
}

t = text[language]

# TITLE
st.title(t["title"])
st.markdown(t["desc"])


# USER INPUT
name = st.text_input(t["name"])
sleep = st.slider(t["sleep"], 0.0, 12.0, 7.0)
phone_use = st.slider(t["phone"], 0.0, 6.0, 2.0)
travel = st.slider(t["travel"], 0, 120, 30)

# ANALYSIS
if st.button(t["analyze"]):

    sleep_debt = max(0, 8 - sleep)
    stress_score = int(sleep_debt * 12)

    if sleep < 5:
        stress = "Very High"
    elif sleep < 6:
        stress = "High"
    elif sleep < 7:
        stress = "Moderate"
    else:
        stress = "Healthy"

    st.subheader(t["results"])
    st.write("Name:", name)
    st.write(t["stress"], ":", stress)
    st.write(t["score"], ":", stress_score)

    if stress_score < 20:
        st.success(t["excellent"])
    elif stress_score < 40:
        st.info(t["fair"])
    elif stress_score < 70:
        st.warning(t["risk"])
    else:
        st.error(t["highrisk"])

    # Academic focus prediction
    st.subheader("Academic Focus Prediction")

    if sleep < 5:
        st.error("Very low focus expected in school today.")
    elif sleep < 6:
        st.warning("Reduced concentration expected.")
    elif sleep < 7:
        st.info("Moderate focus level.")
    else:
        st.success("Good cognitive performance expected.")

    # Study planning
    st.subheader("Study Planning Suggestion")

    if sleep < 6:
        st.write("Today focus on light revision instead of heavy study.")
    elif sleep < 7:
        st.write("Good day for moderate study sessions.")
    else:
        st.write("Great day for learning new topics.")

    # Sleep recommendation
    target_sleep = 8
    sleep_gap = target_sleep - sleep

    if sleep_gap > 0:
        st.write(f"{t['recommend']} {sleep_gap:.1f} hours.")
    else:
        st.write(t["great"])

    if phone_use > 2:
        st.warning(t["phonewarn"])

    if travel > 60:
        st.warning(t["travelwarn"])

    if sleep < 6:
        st.warning(t["focuswarn"])

# Habit Tracker
st.subheader(t["habits"])

habit1 = st.checkbox(t["habit1"])
habit2 = st.checkbox(t["habit2"])
habit3 = st.checkbox(t["habit3"])
habit4 = st.checkbox(t["habit4"])
habit5 = st.checkbox(t["habit5"])

habits_done = sum([habit1, habit2, habit3, habit4, habit5])

st.write(t["completed"], habits_done, "/5")
st.progress(habits_done / 5)

if habits_done == 5:
    st.success(t["champ"])
    st.balloons()
elif habits_done >= 3:
    st.info(t["good"])
elif habits_done >= 1:
    st.warning(t["keep"])
else:
    st.error(t["start"])

st.caption(t["caption"])
st.markdown("### Give Feedback")
st.markdown("[Student Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSdvJfg6Bz4Zvn4NjEJ_h6gfYOxLzEaS3bbI8YavTcqaZ8rPiw/viewform?usp=sf_link)")
