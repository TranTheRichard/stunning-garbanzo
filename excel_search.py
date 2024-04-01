import streamlit as st
import pandas as pd
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1554995207-c18c203602cb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
file_path = "namelist.xlsx"
df = pd.read_excel(file_path)

def main():
    st.title("Finding a homie")
    search_name = st.text_input("Enter a name to search:")

    if st.button("Search"):
        result = search_dataframe(df, search_name)
        if result is not None:
            st.write("Homie found:")
            st.write(result)
        else:
            st.write("No Homie found.")

def search_dataframe(df, search_name):
    result = df[df['Name'].str.lower() == search_name.lower()]
    if not result.empty:
        return result
    else:
        return None

if __name__ == "__main__":
    main()

