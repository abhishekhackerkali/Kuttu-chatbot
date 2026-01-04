import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Kuttu", page_icon="🤖")

st.title("🤖 Kuttu")
st.write("A simple chatbot built using Python and Streamlit")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Kuttu", response))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")