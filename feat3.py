import streamlit as st
from audio_recorder_streamlit import audio_recorder
from openai import OpenAI
homie=OpenAI(api_key="")

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1511389026070-a14ae610a1be?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def transcribe_text_to_voice(audio_location):
    audio_file = open(audio_location, "rb")
    transcript = homie.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcript.text

def create_profile(text):
    response = homie.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages = [
            {
                "role": "system",
                "content": "You are a highly skilled AI trained to make profiles based on the audio file contents. The profiles are neatly organized and easy to read."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

st.title("Audio Analysis and Profile Creation")
st.write("Please give a brief description on who you are and what you're looking for in terms of housing.")

recording_duration = st.slider("Recording Duration (seconds)", min_value=10, max_value=120, value=60, step=10)

audio_bytes = audio_recorder(recording_duration)
if audio_bytes:
    audio_location = "audio_file.wav"
    with open(audio_location, "wb") as f:
        f.write(audio_bytes)

    text = transcribe_text_to_voice(audio_location)
    st.write("Does the information here look correct? If not please record once again.")
    st.write(text)

    continue_recording = st.button("Continue")
    if continue_recording:
        api_response = create_profile(text)
        st.write("Here is your Homie Profile:")
        st.write(api_response)
    else:
        st.write("")