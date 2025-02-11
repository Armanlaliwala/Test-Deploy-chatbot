import streamlit as st
import requests

# Rasa server URL
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

st.title("Rasa Chatbot")
st.write("Chat with your AI-powered assistant.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.text_input("You:", "", key="user_input")
if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Send message to Rasa server
    response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_input})
    bot_responses = response.json()
    
    # Display bot response
    for bot_response in bot_responses:
        bot_message = bot_response.get("text", "")
        st.session_state.messages.append({"role": "assistant", "content": bot_message})
        with st.chat_message("assistant"):
            st.markdown(bot_message)
