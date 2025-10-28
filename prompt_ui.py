from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research tools")

user_input = st.text_input("Enter your prompt here:")
if st.button("Summarize"):
    result = st.model.invoke(user_input)
    st.write(result.content)




