# 🤖 Gemini AI Chatbot

A simple AI chatbot built with **Python** and **Google Gemini API**.
The chatbot uses a system prompt to control the AI's behavior and runs continuously through an interactive terminal loop.

## 🚀 Features

* 🤖 Google Gemini integration
* 💬 Interactive command-line chatbot
* 🧠 Custom system prompt
* 🔄 Continuous conversation loop
* 🔐 API key stored securely using `.env`
* 🛑 Type `exit` to stop the chatbot

## 🛠️ Tech Stack

* Python
* Google GenAI SDK
* Google Gemini
* python-dotenv

## 📁 Project Structure

```text
chatbot/
│
├── chatbot/
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> `.env` is ignored by Git and should never be pushed to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

```bash
cd chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your real API key to GitHub.

## ▶️ Run the Chatbot

```bash
python chatbot/main.py
```

You should see:

```text
You:
```

Enter your question:

```text
You: What is Python?
AI👉 Python is a high-level programming language...
```

To stop the chatbot:

```text
You: exit
```

## 🧠 How It Works

The chatbot sends the user's query along with a predefined system instruction to the Gemini model.

```text
User Query
    ↓
System Prompt
    ↓
Gemini Model
    ↓
AI Response
    ↓
Terminal
```

The system prompt defines how the AI should behave.

Example:

```python
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer according to the user's query.
Keep your answers short and clear.
"""
```

## 📦 Requirements

Example `requirements.txt`:

```text
google-genai
python-dotenv
```

## 🔐 Security

API keys and other secrets should **never** be committed to GitHub.

The `.gitignore` file contains:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## 🔮 Future Improvements

* [ ] Add conversation memory
* [ ] Add streaming responses
* [ ] Add multiple AI tools
* [ ] Add function/tool calling
* [ ] Add web search
* [ ] Convert chatbot into a FastAPI API
* [ ] Build an Agentic AI workflow
* [ ] Add LangGraph

## 👨‍💻 Author

**Asad Azam**

B.Tech CSE | MERN Stack Developer → GenAI / AI Engineer

---

⭐ If you find this project useful, consider giving it a star!

