import os
import streamlit as st
import asyncio
import logging
from typing import AsyncIterable
from groq import Groq  # Assuming Groq is installed and imported correctly

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Groq client
client = Groq(api_key="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")

# System message for context in mortgage assistant
system_message = """You are an AI assistant specializing in the education industry"""

# Helper function to ensure roles are valid
def validate_messages(messages):
    for i, message in enumerate(messages):
        if message.get("role") not in {"system", "user", "assistant"}:
            logger.error("Invalid role in message %d: %s", i, message)
            raise ValueError(f"Invalid role in message {i}: {message}")

# Helper function to convert Streamlit messages to Groq messages
def convert_messages_to_groq(messages):
    validate_messages(messages)  # Validate roles before conversion
    converted = [{"role": msg["role"], "content": msg["content"]} for msg in messages]
    logger.info("Converted messages to Groq format: %s", converted)
    return converted

async def async_generate_response(query: str, chat_history: list) -> AsyncIterable[str]:
    # Append user message to chat history and validate
    chat_history.append({"role": "user", "content": query})
    validate_messages(chat_history)  # Ensure no invalid roles before sending

    # Create a new chat completion using Groq API
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=convert_messages_to_groq(chat_history),
        temperature=1.0,
        max_tokens=1024,
        top_p=1.0,
        stream=True,
        stop=None
    )

    # Stream and yield each response chunk
    for chunk in completion:
        yield chunk.choices[0].delta.content or ""

async def generate_and_display_response(prompt: str):
    with st.chat_message("human"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Collect response chunks and display in real-time
        async for response_chunk in async_generate_response(prompt, st.session_state['messages']):
            full_response += response_chunk
            message_placeholder.markdown(full_response + "▌")
        
        # Display the complete response
        message_placeholder.markdown(full_response)

    # Update session state with user and assistant messages
    st.session_state['messages'].append({"role": "user", "content": prompt})
    st.session_state['messages'].append({"role": "assistant", "content": full_response})

# Wrapper to ensure that asyncio tasks run in Streamlit
def run_async_task(coro):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # No running event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

def main():
    st.title("Student Assistant")

    # Initialize session state for storing messages
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [{"role": "system", "content": system_message}]

    # Display chat history from previous messages
    for message in st.session_state['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input handling
    if prompt := st.chat_input("What would you like to know about education?"):
        run_async_task(generate_and_display_response(prompt))  # Use wrapper for async function

    # Disclaimer and Styling
    st.markdown("---")
    st.write("**Disclaimer:** THIS IS AN AI RESPONSE AND MAY BE WRONG")

    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Explore the Power of Student Assistant</p>', unsafe_allow_html=True)

    # Sidebar with additional info and sample questions
    st.sidebar.title("About")
    st.sidebar.info("This is a chatbot that will help you get more mnarks")

    st.sidebar.title("Sample Questions")
    sample_questions = [
        "What is FERPA, and how does it protect student information?", 
        "How is a GPA calculated, and why is it important in academic evaluations?", 
        "What are the key differences between formative and summative assessments?",
         "How does attendance tracking affect student performance metrics?",
          "What is the significance of standardized test scores in educational systems?",
           "What is the role of student feedback in course improvement?", 
           "What is a student ID, and how is it used in academic institutions?",
            "What are the common challenges in managing student records?", 
            "How does socioeconomic data influence education policy decisions?", 
        "What is a student cohort, and why is it analyzed in education research?"
    ]

    for question in sample_questions:
        if st.sidebar.button(question):
            run_async_task(generate_and_display_response(question))  # Use wrapper for async function

if __name__ == "__main__":
    main()
