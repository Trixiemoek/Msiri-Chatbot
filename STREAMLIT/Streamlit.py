import streamlit as st
from rasa.core.agent import Agent
rasa_agent = Agent.load(r"C:\Users\HomePC\Documents\Mental Health\Msiri_project\MODEL\20240425-203440-charcoal-mayonnaise.tar.gz")
# Streamlit title and header
st.title("Msiri")
st.header("Msiri keeps your Secrets")

# Text input for user input
user_input = st.text_input("You:", "")

# Button to send user input
if st.button("Send"):
    # Call Rasa to get bot response
    bot_response = rasa_agent.handle_text(user_input)
    # Display bot response
    st.text("Bot:", bot_response[0]['text'])
