from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
import requests
from fastapi.responses import FileResponse
from dotenv import load_dotenv

# Load API key securely from .env
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Rachel's voice ID (you can change it)

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
        text = result["text"]
        
        # Generate speech using ElevenLabs API
        audio_path = generate_speech(text)
        if not audio_path:
            raise HTTPException(status_code=500, detail="Failed to generate speech.")

        return {
            "transcription": text,
            "audio_url": "/get_audio"
        }
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)  # Clean up

@app.get("/get_audio")
async def get_audio():
    """Serve the generated audio file."""
    return FileResponse("story_audio.mp3", media_type="audio/mpeg", filename="story.mp3")

def generate_speech(text):
    """Uses ElevenLabs API to generate speech and save as an MP3 file."""
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
