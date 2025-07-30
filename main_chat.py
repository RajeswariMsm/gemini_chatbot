from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY']="your_secret_key_here"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model=genai.GenerativeModel("gemini-2.5-flash")
chat=model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
st.set_page_config(page_title="Chatbot demo")
st.header("Gemini LLM Application")
if "chat_history" not in st.session_state:
   st.session_state["chat_history"]=[]
input=st.text_input("input:",key="input")   
submit=st.button("Ask the Question")
if submit and input:
    response=get_gemini_response(input)
    st.subheader("The response is")
    chunk=[]
    for chunk in response:
        st.write(chunk.text)
       
