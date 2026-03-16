import streamlit as st

# Language selection
language = st.selectbox("Select Language / ഭാഷ തിരഞ്ഞെടുക്കുക", ["English", "Malayalam"])

text = {

"English":{

"title":"Sleep Habit Tracker",

"habit1":"Sleep before 11 PM",
"habit2":"Avoid phone 1 hour before sleep",
"habit3":"Morning sunlight",
"habit4":"Exercise 20 minutes",
"habit5":"No caffeine after evening",

"completed":"Habits completed",
"champ":"🏆 Sleep Champion",
"good":"⭐ Good Progress",
"keep":"⚡ Keep Building Healthy Habits",
"start":"Start building healthy sleep habits today",

"caption":"Educational sleep awareness tool for students."
},

"Malayalam":{

"title":"ഉറക്ക ശീലങ്ങൾ ട്രാക്കർ",

"habit1":"11 മണിക്ക് മുമ്പ് ഉറങ്ങുക",
"habit2":"ഉറങ്ങാൻ 1 മണിക്കൂർ മുമ്പ് ഫോൺ ഒഴിവാക്കുക",
"habit3":"പ്രഭാത സൂര്യപ്രകാശം",
"habit4":"20 മിനിറ്റ് വ്യായാമം",
"habit5":"വൈകുന്നേരത്തിന് ശേഷം കഫെയ്ൻ ഒഴിവാക്കുക",

"completed":"പൂർത്തിയാക്കിയ ശീലങ്ങൾ",
"champ":"🏆 ഉറക്ക ചാമ്പ്യൻ",
"good":"⭐ നല്ല പുരോഗതി",
"keep":"⚡ ആരോഗ്യ ശീലങ്ങൾ തുടരുക",
"start":"ആരോഗ്യകരമായ ഉറക്ക ശീലങ്ങൾ തുടങ്ങുക",

"caption":"വിദ്യാർത്ഥികൾക്കുള്ള ഉറക്ക ബോധവൽക്കരണ ഉപകരണം."
}

}

t = text[language]

st.title(t["title"])

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
