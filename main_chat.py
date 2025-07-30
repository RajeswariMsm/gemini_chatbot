rom dotenv import load_dotenv           # For loading environment variables from a .env file
import streamlit as st                   # Streamlit for building web apps
import os
import google.generativeai as genai      # Gemini generative AI SDK

# Set Google API key for authentication (replace with your actual key or use load_dotenv for security)
os.environ['GOOGLE_API_KEY'] = "your_secret_key_here"

# Configure Gemini API with the provided key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create a generative model instance (using Gemini 2.5 flash)
model = genai.GenerativeModel("gemini-2.5-flash")

# Start a chat session with empty history
chat = model.start_chat(history=[])

# Function to get response from Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)  # Send question to Gemini, receive streamed response
    return response

# Streamlit page configuration
st.set_page_config(page_title="Chatbot demo")
st.header("Gemini LLM Application")

# Initialize chat history in Streamlit session state if not present
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input box for user question
input = st.text_input("input:", key="input")
submit = st.button("Ask the Question")   # Button to submit the question

# When user submits a question
if submit and input:
    response = get_gemini_response(input)    # Get response from Gemini
    st.subheader("The response is")
    chunk = []
    # Stream and display each chunk of Gemini's response
    for chunk in response:
        st.write(chunk.text)
