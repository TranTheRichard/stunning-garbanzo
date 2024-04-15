import streamlit as st
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

def transcribe_audio(audio_file):
    transcription = homie.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text

def create_profile(transcription):
    response = homie.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled an AI trained to make profiles based on the audiofile contents. The profiles are neatly organized and is easy to read."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

def analyze_audio(audio_file):
    return f"Audio file uploaded: {audio_file.name}"

def main():
    st.title("Audio Analysis and Profile Creation")
    st.write("Upload an audio file to make a Homie profile.")

    audio_file = st.file_uploader("Please upload Audio File", type=["mp3", "wav"])

    if audio_file is not None:
        st.audio(audio_file, format='audio/wav', start_time=0)

        if st.button("Analyze and create Profile"):
            analysis_result = analyze_audio(audio_file)
            st.write("Analysis Result:")
            st.write(analysis_result)

            transcription = transcribe_audio(audio_file)
            profile = create_profile(transcription)

            st.write("Homie Profile:")
            st.write(profile)
                
if __name__ == "__main__":
    main()