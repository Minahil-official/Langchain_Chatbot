# Adding Key to my file

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the GOOGLE_API_KEY from the environment
api_key = os.getenv("GOOGLE_API_KEY_2")


# Check if the API key is loaded correctly
if api_key:
    print(f"Your API Key is found")
else:
    print("API Key is not found. Please check your .env file.")

# Importing classes from langchain
 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

import streamlit as st



llm = ChatGoogleGenerativeAI(
    api_key = api_key,
    model = "gemini-2.0-flash-exp",
    temperature = 0.5
)

initial_prompt = PromptTemplate(
    input_variables = ["question"],
    template = "change the {question} to a text generation prompt")




st.title("Chatbot with Gemini-2.0")
st.write("Welcome to Langchain Chatbot")
st.markdown("You can get answer of your queries here")
 
 
with st.form("user_input_form"):
    user_input = st.text_input("Type your question here:")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    if user_input.strip():
        # Create the chain
        chain = initial_prompt | llm
        try:
            # Invoke the chain with the user input
            first_response = chain.invoke({"question": user_input})
            st.success("Response:")
            st.write(first_response.content)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid input!")


