import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
     st.session_state.messages = []


for message in st.session_state.messages:
     with st.chat_message(message["role"]):
         st.write(message["content"])


if prompt := st.chat_input("Ask me anything..."):

     st.session_state.messages.append(
         {"role": "user", "content": prompt}
     )

     with st.chat_message("user"):
         st.write(prompt)

     response = client.chat.completions.create(
         model="llama-3.3-70b-versatile",
         messages=st.session_state.messages
     )

     answer = response.choices[0].message.content

     st.session_state.messages.append(
         {"role": "assistant", "content": answer}
     )

     with st.chat_message("assistant"):
         st.write(answer)


