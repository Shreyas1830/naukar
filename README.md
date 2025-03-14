# Chikki A.I.

Chikki A.I. is a **voice-based virtual assistant** that can perform various tasks, including opening websites, playing music, fetching weather updates, chatting using AI, and more. Built with Python, it utilizes **speech recognition, text-to-speech (TTS), and AI-powered chat capabilities** to assist users in a natural and interactive way.

## 🚀 Features
- **Voice Commands**: Interact using voice inputs.
- **AI Chatbot**: Engages in conversations using the Together AI API.
- **Weather Updates**: Fetch real-time weather using WeatherAPI.
- **System Automation**: Open websites, play Spotify, check the time, and more.
- **Camera Access**: Open the system camera with a command.
- **Speech Output**: Uses text-to-speech to respond audibly.

## 🛠 Tech Stack
- **Python**
- **SpeechRecognition** (for voice commands)
- **win32com.client** (for text-to-speech)
- **Together AI API** (for chatbot interactions)
- **WeatherAPI** (for real-time weather updates)
- **Requests** (for API calls)

## 🔧 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/chikki-ai.git
cd chikki-ai
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
- Get a free **WeatherAPI** key from [WeatherAPI.com](https://www.weatherapi.com/).
- Get a **Together AI** API key from [Together AI](https://www.together.xyz/).
- Replace `API_KEY` in `get_weather()` and `Together(api_key="YOUR_API_KEY")` with your respective keys.

## 🏃‍♂️ Usage
Run the assistant using:
```bash
python chikki_ai.py
```

### Example Commands:
- "**Open YouTube**"
- "**What's the weather in Mumbai?**"
- "**What time is it?**"
- "**Using Artificial Intelligence, write a poem**"
- "**Chikki Quit**" (to exit)

## 🤝 Contributing
1. **Fork the repository**
2. **Create a new branch** (`feature-branch`)
3. **Commit changes**
4. **Push to your fork**
5. **Open a Pull Request**



---
💡  🚀 Happy Coding!

