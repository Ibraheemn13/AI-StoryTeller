from fastapi import FastAPI, UploadFile, File
import whisper
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domains for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Storyteller API is running!"}


# Load Whisper model once during startup
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
        return {"transcription": result["text"]}
    
    finally:
        # Clean up the file after processing
        if os.path.exists(file_path):
            os.remove(file_path)


