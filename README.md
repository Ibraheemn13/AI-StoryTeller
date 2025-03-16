# AI-StoryTeller
# AI Storyteller - README

Welcome to **AI Storyteller**, a web application that allows children to **speak or type an idea**, generates a **creative story** using **Google Gemini AI**, and narrates it back using **ElevenLabs AI voice**. The interactive UI includes a **talking robot**, **playback controls**, and an **edit story option**.

---

## Features
✅ **Speech-to-Text**: Uses **Whisper AI** to transcribe spoken words  
✅ **AI Story Generation**: Generates a fun story using **Google Gemini AI**  
✅ **Text-to-Speech (TTS)**: Converts the story into **natural narration** using **ElevenLabs**  
✅ **Interactive UI**: Play/pause controls, robot animations, and dynamic layout  
✅ **Type & Edit Option**: Users can type their own idea and edit the generated story  

---

## Tech Stack
- **Frontend**: HTML, Tailwind CSS, JavaScript  
- **Backend**: FastAPI (Python)  
- **AI Models**: Whisper AI, Google Gemini AI, ElevenLabs TTS  
- **Hosting**: Local server 

---

## How to Install & Run the Project Locally

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ibraheemn13/AI-Storyteller.git
cd AI-Storyteller
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Get API Keys
To use **Google Gemini AI** and **ElevenLabs**, get API keys:  
- **Google Gemini AI**: [Get API Key](https://ai.google.dev)  
- **ElevenLabs**: [Get API Key](https://elevenlabs.io)  
- **Whisper AI**: No API key needed, but ensure **ffmpeg** is installed.

Add these API keys to a `.env` file:  
```sh
GEMINI_API_KEY=your_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=your_selected_voice_id
```

### 5️⃣ Run the Backend Server
```sh
uvicorn main:app --reload
```
- The API runs at **`http://127.0.0.1:8000`**  
- Visit **`http://127.0.0.1:8000/docs`** for API testing  

### 6️⃣ Run the Frontend
Just open `index.html` in a web browser!  

---

## How to Use
1️⃣ Click **"Speak Your Idea"** and start talking  
2️⃣ AI generates a **story & narration**  
3️⃣ Play the story **using the play button**  
4️⃣ Enjoy the **story**

---

## API Endpoints
| **Method** | **Endpoint** | **Description** |
|------------|-------------|----------------|
| `POST` | `/transcribe/` | Transcribes speech or accepts typed input |
| `POST` | `/generate_story/` | Uses Gemini AI to create a story |
| `POST` | `/synthesize_speech/` | Converts text to speech (ElevenLabs) |
| `GET` | `/get_audio` | Fetches generated audio for playback |

---

## Customization
- **Change AI Voices**: Update **ELEVENLABS_VOICE_ID** in `.env`  
- **Modify UI Design**: Edit **index.html & styles.css**  
- **Deploy to Cloud**: Use **AWS, Heroku, Render, or Vercel**  

---

## Troubleshooting
**Microphone Not Working?**  
 Ensure browser **allows microphone access**  

**Voice Not Found (ElevenLabs Error)?**  
 **Check voice ID** in `.env` and ensure **ElevenLabs API key is correct**  

**Whisper AI Not Running?**  
 Install **ffmpeg**:  
```sh
pip install ffmpeg-python
```

**Backend Not Starting?**  
 Check if **Uvicorn is installed**:
```sh
pip install uvicorn
```

---

## 🌟 Contributors
👨‍💻 Developed by **[Muhammad Ibraheem Noor]**  
💬 Feel free to contribute by **forking the repo & making PRs!**  

---

## 📜 License
📝 **MIT License** - Feel free to modify and use this project!  

---