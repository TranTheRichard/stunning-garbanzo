import streamlit as st
from openai import OpenAI

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1511389026070-a14ae610a1be?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

homie = OpenAI(api_key="")
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = homie.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a chatbot that is helping with affordable housing and is knowledgeable on what places are good to live in based on what inputs are given. While also formatting the information in a neat and organized way."},
            {"role": "user", "content": prompt},
        ]
    )
    if completion.choices:
        return completion.choices[0].message.content
    else:
        return "Sorry, unable to generate a response for this prompt."

def main():
    menu_selection = st.sidebar.radio("Menu", ["Home","Chat", "About", "Contact"])

    if menu_selection == "Home":
        st.title("Welcome to Housing Haven")

    elif menu_selection == "Chat":
        st.title("Housing Haven AI Chatbot")
        with st.form(key="chat"):
            st.write("Please provide the following information:")
            name = st.text_input("Your Name:")
            location = st.text_input("Your Location:")
            situation = st.text_area("Describe your current situation:")
            income = st.number_input("Annual Income:", min_value=0, step=10000)
            other_info = st.text_area("Any other information you wish to provide:")

            submitted = st.form_submit_button("Submit")

            if submitted:
                prompt = f"Name: {name}\nLocation: {location}\nSituation: {situation}\nAnnual Income: {income}\nOther Information: {other_info}\n"
                response = get_completion(prompt)
                st.write("Housing Haven AI:", response)

    elif menu_selection == "About":
        st.write('''
            Welcome to our About page, we are Housing haven. Our goal is to help provide information on what to do about housing based on your own information that you have provided. 

            We have three main features.
            1. Our chat box where a Model asks for these in order from the user: name, location, situation, annual income, any other information that the user wishes to provide to the model to better help equip themselves. 
            2. The second takes the given or preferred location(s) and eligibility based on tax forms, bills, see if you are filed as an independent or dependent to match you with a program that is best to assist the customer. 
            3. The last one analyzes an audio file and creates a profile based on the audio contents.
''')
        
    elif menu_selection == "Contact":
        st.write("Contact us at housinghaven@gmail.com")

if __name__ == "__main__":
    main()
