import streamlit as st

st.set_page_config(
    page_title="Student Sleep Health Analyzer",
    page_icon="🌙",
    layout="centered"
)

# Hide Streamlit menu/footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Language selection
language = st.selectbox("Select Language / ഭാഷ തിരഞ്ഞെടുക്കുക", ["English", "Malayalam"])

# Text dictionary
text = {

"English":{

"title":"Student Sleep Health Analyzer 🌙",

"intro":"""
A simple digital wellness tool designed to help students understand how
sleep habits, phone usage, and travel fatigue may affect stress levels
and academic focus.
""",

"problem_title":"Problem",

"problem":"""
Many students experience sleep deprivation due to late phone use,
academic pressure, and long school travel time.

Poor sleep can affect concentration, memory, mood, and learning ability.
""",

"solution_title":"What This Tool Helps You Do",

"solution":"""
• Analyze sleep health and stress level  
• Predict academic focus for the day  
• Get simple study planning suggestions  
• Track healthy sleep habits
""",

"tools_title":"Tools Available",

"tools":"""
Use the sidebar to navigate through the tool:

• **Sleep Analyzer** – Analyze how sleep, phone use, and travel fatigue affect stress.

• **Habit Tracker** – Track healthy daily habits that improve sleep quality.
""",

"feedback":"Give Feedback"

},

"Malayalam":{

"title":"വിദ്യാർത്ഥികളുടെ ഉറക്ക ആരോഗ്യ വിശകലന ഉപകരണം 🌙",

"intro":"""
ഉറക്ക ശീലങ്ങൾ, ഫോൺ ഉപയോഗം, യാത്ര ക്ഷീണം എന്നിവ
വിദ്യാർത്ഥികളുടെ സമ്മർദ്ദത്തെയും പഠന ശ്രദ്ധയെയും എങ്ങനെ ബാധിക്കുന്നു
എന്ന് മനസ്സിലാക്കാൻ സഹായിക്കുന്ന ഒരു ലളിതമായ ഡിജിറ്റൽ ഉപകരണം.
""",

"problem_title":"പ്രശ്നം",

"problem":"""
പല വിദ്യാർത്ഥികളും രാത്രിയിലെ ഫോൺ ഉപയോഗം,
പഠന സമ്മർദ്ദം, ദീർഘമായ യാത്ര സമയം എന്നിവ കാരണം
ഉറക്കക്കുറവ് അനുഭവിക്കുന്നു.

ഉറക്കക്കുറവ് ശ്രദ്ധ, ഓർമ്മശക്തി, പഠനക്ഷമത എന്നിവയെ ബാധിക്കാം.
""",

"solution_title":"ഈ ടൂൾ നിങ്ങളെ സഹായിക്കുന്നത്",

"solution":"""
• ഉറക്ക ആരോഗ്യവും സമ്മർദ്ദ നിലയും വിലയിരുത്തുക  
• ദിവസത്തെ പഠന ശ്രദ്ധ പ്രവചിക്കുക  
• ലളിതമായ പഠന പദ്ധതി നിർദ്ദേശങ്ങൾ ലഭിക്കുക  
• ആരോഗ്യകരമായ ഉറക്ക ശീലങ്ങൾ ട്രാക്ക് ചെയ്യുക
""",

"tools_title":"ലഭ്യമായ ടൂളുകൾ",

"tools":"""
സൈഡ്‌ബാർ ഉപയോഗിച്ച് ടൂളുകൾ തുറക്കുക:

• **Sleep Analyzer** – ഉറക്കം, ഫോൺ ഉപയോഗം, യാത്ര ക്ഷീണം എന്നിവ സമ്മർദ്ദത്തെ എങ്ങനെ ബാധിക്കുന്നു എന്ന് പരിശോധിക്കുക.

• **Habit Tracker** – ആരോഗ്യകരമായ ഉറക്ക ശീലങ്ങൾ ട്രാക്ക് ചെയ്യുക.
""",

"feedback":"അഭിപ്രായം നൽകുക"

}

}

t = text[language]

# Title
st.title(t["title"])

# Introduction
st.markdown(t["intro"])

# Problem
st.markdown(f"### {t['problem_title']}")
st.markdown(t["problem"])

# Solution
st.markdown(f"### {t['solution_title']}")
st.markdown(t["solution"])

# Tools
st.markdown(f"### {t['tools_title']}")
st.markdown(t["tools"])

# Feedback
st.markdown(f"### {t['feedback']}")
st.markdown("[Student Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSdvJfg6Bz4Zvn4NjEJ_h6gfYOxLzEaS3bbI8YavTcqaZ8rPiw/viewform?usp=sf_link)")