import streamlit as st 
from openai import OpenAI
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1554995207-c18c203602cb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

client = OpenAI(api_key="") 
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion =client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system","content": "You are a chatbot that is helping with affordable housing"},
        {"role":"user","content":prompt},
        ]
    )
    if completion.choices:
        return completion.choices[0].message.content
    else:
        return "Sorry, unable to generate a response for this prompt."

with st.form(key = "chat"):
    prompt = st.text_input("Hello, this Housing Haven AI chatbot, how can I Help you?")
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if prompt.lower()=='exist':
            st.stop
        else:
            response=get_completion(prompt)
            st.write(response)