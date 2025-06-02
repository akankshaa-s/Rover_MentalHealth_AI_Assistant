# 🧠 Rover_MentalHealth_AI_Assistant

Rover is an empathetic, multilingual AI-powered mental health assistant designed to provide supportive, non-judgmental conversations through speech.  
It combines the power of large language models (LLMs), speech-to-text (STT), and text-to-speech (TTS) technologies to create a seamless spoken interaction in your preferred language.

---

## 🎯 Features

- 🎙️ **Voice Interaction** using Whisper (OpenAI) for speech recognition  
- 🧠 **Conversational AI** with LangChain + Llama3 via Ollama  
- 🌍 **Multilingual Support** (English, Hindi, Kannada) via Google Translate  
- 🗣️ **Speech Response** using gTTS (Text-to-Speech)  
- 💾 **Chat History Saving** with timestamped `.txt` files  
- 🔁 **Session Management** – Start, continue, or exit conversations easily  
- ⚙️ **Integrated Ollama Runtime Control** – Starts and stops `ollama` server within the app  

---

## 🛠️ Tech Stack

| Component            | Tech Used                             |
|----------------------|----------------------------------------|
| Interface            | Streamlit                              |
| Speech-to-Text       | Whisper (OpenAI)                       |
| Text-to-Speech       | gTTS + Pydub                           |
| Translation          | Deep Translator                        |
| LLM Integration      | LangChain + Ollama (LLaMA3.2 model)    |
| Language Models      | LLaMA3.2 via `OllamaLLM`               |
| Context Handling     | LangChain `ChatPromptTemplate`         |

---

## 🧪 How It Works

1. **Voice Input**: User speaks, and Whisper transcribes the voice  
2. **Translation**: If input is not in English, it is translated to English  
3. **Context Retrieval**: Last 3 exchanges are passed as context to the LLM  
4. **AI Response**: LLaMA3.2 generates an empathetic reply  
5. **Translate & Speak**: Response is translated back and spoken out loud  
6. **Session Control**: Users can continue, end, or save conversations  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rover-mental-health-ai.git
cd rover-mental-health-ai
```

### 2.  Install Dependencies

```bash
pip install -r requirements.txt
```
Required packages:

1. streamlit

2. langchain

3. langchain_ollama

4. deep-translator

5. whisper

6. gtts

7. pydub

8. sounddevice

9. scipy

### 3.  Run Ollama Server

Manual Setup : 

```bash
ollama serve
```
Automatic setup:

The Streamlit app will also auto-start ollama server when we click "Start talking" button.

### 4.  Run the App

```bash
streamlit run chatbot.py
```

📁 Project Structure

```nginx
Whisper model/
├── chatbot.py            # Main Streamlit application
├── stt.py                # Speech-to-Text using Whisper
├── tts.py                # Text-to-Speech using gTTS and Pydub
├── Finetune_Whisper.py   # (Optional) Fine-tuning Whisper
├── counselchat-data.csv  # Dataset for chatbot training/fine-tuning
├── *.txt                 # Chat history logs
```

📌 Notes
1. Make sure to install ffmpeg (required by pydub)

2. Whisper runs on CPU by default with tiny model – upgrade to base or medium if needed

3. Ollama must be installed and accessible from terminal
   

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### Author Akanksha S 🙋‍♀️

* GitHub - https://github.com/akankshaa-s/
* LinkedIn - https://www.linkedin.com/in/akanksha-s-7216471a6/

---------------------------------------------------------------------------------------------------------------







