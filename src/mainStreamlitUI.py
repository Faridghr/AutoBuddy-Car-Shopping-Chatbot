from chatBot import ChatBot
import streamlit as st
import json

material_file_path = './Materials/CarsInformation.txt'
bot = ChatBot(material_file_path)

st.title('AutoBuddy: A Car Shopping Search Chatbot')

# Store LLM generated responses
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm AutoBuddy. How can I assist you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Getting your answer from our knowledge base..."):
                response = bot.generate_response(input)
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)
