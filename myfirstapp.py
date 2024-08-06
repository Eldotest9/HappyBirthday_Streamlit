import streamlit as st

st.balloons()
st.title("Happy Birthday 🎈")


slider_value = st.slider('Select a value', min_value=0, max_value=100, value=50)
if (slider_value <51):
    VIDEO_URL = "https://www.youtube.com/watch?v=NT3zp2vYMvo"
else:
    VIDEO_URL = "https://www.youtube.com/watch?v=Ctf2g_-VZbo&ab_channel=ShyamPankhania"


st.video(VIDEO_URL,start_time=0)




