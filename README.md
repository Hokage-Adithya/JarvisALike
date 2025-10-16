# 🧠 JARVIS - Your Personal AI Voice Assistant

JARVIS is a Python-based **voice assistant** that listens to your voice commands, performs tasks like opening websites, playing music, fetching the latest news, and can even **chat intelligently** using **Google Gemini AI**.

---

## 🚀 Features

* 🎤 **Voice Activation:** Say “Jarvis” to wake the assistant.
* 🌐 **Web Commands:** Open Google or YouTube directly.
* 🎶 **Music Player:** Play songs from a predefined music library (`music_library.py`).
* 📰 **News Reader:** Fetch and read top headlines using the **NewsAPI**.
* 🧩 **AI Conversations:** Uses **Gemini 1.5 Flash** model for smart responses.
* 🗣️ **Text-to-Speech:** Responds with natural speech using `pyttsx3`.

---

## 🧩 Project Structure

```
JARVIS/
│
├── jarvis.py                 # Main assistant script
├── music_library.py          # Music dictionary (song name: URL)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For Linux/Mac
```

### 3️⃣ Install Dependencies

Create a `requirements.txt` file containing:

```
SpeechRecognition
pyttsx3
requests
google-generativeai
```

Then install:

```bash
pip install -r requirements.txt
```

> 💡 If `pyaudio` fails to install on Windows:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🔑 API Keys

### 📰 News API

* Get a free API key from [NewsAPI.org](https://newsapi.org/).
* Replace the `newsapi` variable in `jarvis.py`:

  ```python
  newsapi = "YOUR_NEWS_API_KEY"
  ```

### 🤖 Google Gemini API

* Get your API key from [Google AI Studio](https://aistudio.google.com/).
* Set it up before using:

  ```python
  import google.generativeai as genai
  genai.configure(api_key="YOUR_GEMINI_API_KEY")
  ```

---

## 🎵 Music Library

Create a file named `music_library.py` with a dictionary of your songs:

```python
music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "attention": "https://www.youtube.com/watch?v=nfs8NYg7yQM"
}
```

---

## 🧠 How It Works

1. JARVIS continuously listens for the keyword **“Jarvis”**.
2. When activated, it asks for your command.
3. Based on what you say, it will:

   * Open websites like Google or YouTube.
   * Play music from your library.
   * Fetch and read current news.
   * Or use **Gemini AI** to reply intelligently.

---

## ▶️ Run the Assistant

```bash
python jarvis.py
```

Then say:

> 🗣️ “Jarvis”
> 🗣️ “Play believer”
> 🗣️ “Open Google”
> 🗣️ “Tell me the latest news”
> 🗣️ “What is AI?”

---

## ⚠️ Notes

* Requires a **working microphone**.
* The assistant uses **Google Speech Recognition**, which needs internet access.
* To make it **fully offline**, you can replace the recognizer with **VOSK** (I can help you with that).

---

## 📜 License

This project is released under the **MIT License** — free to use and modify.

---

## 🧑‍💻 Author

**Adithya Sharma**
🔹 AI/ML Developer | Python Enthusiast | Voice Assistant Builder

