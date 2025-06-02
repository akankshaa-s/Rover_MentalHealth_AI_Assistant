# chatbot.py

import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from deep_translator import GoogleTranslator
from stt import recognize_speech
from tts import speak
import subprocess
import re
from datetime import datetime

# Prompt template
template = """
You are Rover, a compassionate AI mental health assistant. Provide supportive, empathetic, non-judgmental responses.

Here is the recent conversation:

{context}

User: {question}

Rover:"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []  # list of dicts with keys: user, rover
if 'ollama_process' not in st.session_state:
    st.session_state.ollama_process = None
if 'ollama_running' not in st.session_state:
    st.session_state.ollama_running = False

st.set_page_config(page_title="Rover - Mental Health AI", layout="wide")
st.title("🧠 Rover - Your Mental Health Assistant")

# Language settings
language = st.selectbox("Choose your preferred language:", ["English", "Hindi", "Kannada"])
lang_map = {"English": "en", "Hindi": "hi", "Kannada": "kn"}
whisper_lang_map = {"English": None, "Hindi": "hi", "Kannada": "kn"}
lang_code = lang_map[language]

# Show history on sidebar
st.sidebar.title("🗂️ Chat History")
for i, chat in enumerate(st.session_state.history):
    st.sidebar.markdown(f"**{i+1}. You:** {chat['user']}\n\n**🧠 Rover:** {chat['rover']}\n---")

# Start Ollama server if not running
def start_ollama():
    if not st.session_state.ollama_running:
        st.session_state.ollama_process = subprocess.Popen(["ollama", "serve"])
        st.session_state.ollama_running = True
        print("✅ Ollama server started.")

# Stop Ollama server
def stop_ollama():
    if st.session_state.ollama_process:
        st.session_state.ollama_process.terminate()
        st.session_state.ollama_process.wait()
        st.session_state.ollama_process = None
        st.session_state.ollama_running = False
        print("🛑 Ollama server stopped.")

# Format context: only last 3 messages
def get_recent_context():
    history = st.session_state.history[-3:]  # Last 3 turns only
    context = ""
    for chat in history:
        context += f"User: {chat['user']}\nRover: {chat['rover']}\n"
    return context

# Start Talking
if st.button("🎤 Start Talking"):
    if not st.session_state.ollama_running:
        start_ollama()
        st.success("✅ Ollama server started.")

    st.info("🎙️ Listening...")
    user_input = recognize_speech(duration=7, language=whisper_lang_map[language])

    if not user_input:
        st.error("❌ Could not understand. Try again.")
    else:
        st.markdown(f"**You said:** {user_input}")

        try:
            # Translate to English
            english_input = GoogleTranslator(source='auto', target='en').translate(user_input)

            # Get recent conversation context
            context = get_recent_context()

            # Generate response
            response_en = chain.invoke({"context": context, "question": english_input})

            # Translate back
            response_local = GoogleTranslator(source='en', target=lang_code).translate(response_en)

            # Save to history
            st.session_state.history.append({"user": user_input, "rover": response_local})

            st.markdown(f"**🧠 Rover says:** {response_local}")
            speak(response_local, language=lang_code)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
            speak("Sorry, I couldn't understand that.", language=lang_code)

# Continue or Exit buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🔁 Continue Talking"):
        st.rerun()

with col2:
    if st.button("❌ Exit"):
        if st.session_state.history:
            filename = f"rover_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                for h in st.session_state.history:
                    f.write(f"User: {h['user']}\nRover: {h['rover']}\n\n")
            st.success(f"✅ Chat saved as {filename}")
        stop_ollama()
        st.session_state.clear()
        st.success("🛑 Session ended.")
        st.stop()
