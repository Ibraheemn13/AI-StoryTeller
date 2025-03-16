from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
import requests
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import google.generativeai as genai 

# Load API keys securely from .env
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 

# ElevenLabs API settings
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Rachel's voice ID

# Initialize Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Initialize FastAPI
app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Whisper model
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    
    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Transcribe with Whisper
        result = model.transcribe(file_path)
        user_idea = result["text"]
        print(user_idea)        

        # Generate a creative story with Gemini AI
        story = generate_story(user_idea)

        # Convert story to speech using ElevenLabs
        audio_path = generate_speech(story)
        if not audio_path:
            raise HTTPException(status_code=500, detail="Failed to generate speech.")

        return {
            "original_idea": user_idea,
            "generated_story": story,
            "audio_url": "/get_audio"
        }
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)  # Clean up

@app.get("/get_audio")
async def get_audio():
    """Serve the generated audio file."""
    return FileResponse("story_audio.mp3", media_type="audio/mpeg", filename="story.mp3")

def generate_story(user_idea):
    """Generates a fun story for kids using Google's Gemini AI."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Create a short, fun story for kids based on this idea: {user_idea}. Make it engaging, magical, and fun!"

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Error generating story:", str(e))
        return "Once upon a time, in a magical land, an exciting adventure began!"

def generate_speech(text):
    """Converts text into speech using ElevenLabs API."""
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(f"{ELEVENLABS_API_URL}/{VOICE_ID}", json=data, headers=headers)
    
    if response.status_code == 200:
        audio_path = "story_audio.mp3"
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        print("Error generating speech:", response.json())
        return None
