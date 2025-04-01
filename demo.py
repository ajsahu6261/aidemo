import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables and setup Groq client
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Configure Streamlit page
st.set_page_config(
    page_title="AI Chat Interface",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS to make it look more like Google
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        border-radius: 24px;
    }
    .stButton > button {
        border-radius: 24px;
        background-color: #4285f4;
        color: white;
        padding: 0.5rem 2rem;
    }
    .big-title {
        font-size: 72px;
        color: #4285f4;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1 class='big-title'>AI Chat</h1>", unsafe_allow_html=True)

# Create the input field
user_input = st.text_input("", placeholder="Ask a question...")

# Create the submit button
if st.button("Ask"):
    if user_input:
        # Show a spinner while processing
        with st.spinner('Getting response...'):
            # Get response from Groq
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            
            # Display the response
            st.markdown("### Response:")
            st.write(chat_completion.choices[0].message.content)