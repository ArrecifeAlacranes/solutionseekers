import streamlit as st
import google.generativeai as genai

# Get API key
GEMINI_API_KEY = "AIzaSyByuGnvccNx0rjr5G9Bs2CzuJBe9mR59Qo"

# Configure API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel(model_name='gemini-pro')

# Create initial prompt
initial_prompt = """You are a compassionate and supportive virtual therapist specializing in helping students at BMCC manage 
mental health challenges. Your role is to listen attentively, provide helpful insights, and offer practical 
strategies for managing stress, anxiety, and other mental health concerns. You understand the pressures of college 
life, including academic stress, balancing responsibilities, and personal development. Please respond to each student 
with empathy, using simple and encouraging language, and suggest actionable steps they can take to improve their 
well-being. Your goal is to create a safe space for students to feel heard and supported."""

# Initialize chat with initial prompt
chat = model.start_chat()
chat.send_message(initial_prompt)

def main():
    st.title("BMCC Mental Health Support Chat")
    st.write("Welcome! Type your message below to chat with our virtual mental health assistant. Type 'exit' to end the conversation.")

    # Ensure conversation history is maintained in session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Display conversation history
    for message in st.session_state.conversation:
        if message["from"] == "user":
            st.write(f"You: {message['text']}")
        else:
            st.write(f"Assistant: {message['text']}")

    # Input field for user input, displayed after chat history
    user_input = st.text_input("You:", key="user_input")
    
    # Button and Enter key functionality
    if st.button("Send") or user_input:
        if user_input:
            if user_input.lower() == 'exit':
                st.write("Take care! Remember, BMCC Counseling Center: (212) 220-8140")
            else:
                # Get response from the assistant
                response = chat.send_message(user_input)
                st.session_state.conversation.append({"from": "user", "text": user_input})
                st.session_state.conversation.append({"from": "assistant", "text": response.text})
                st.write(f"Assistant: {response.text}")

            # Clear the input field after sending
            st.session_state.user_input = ""  # Resetting text input if needed

if __name__ == "__main__":
    main()
