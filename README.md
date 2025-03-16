<a name="readme-top"></a>

# AI Storyteller | Introduction

**AI Storyteller** is a web application that allows children to **speak or type an idea**, generates a **creative story** using **Google Gemini AI**, and narrates it back using **ElevenLabs AI voice**. The interactive UI includes a **talking robot**, **playback controls**, and an **edit story option** to make storytelling fun and engaging!

#### Read More about it on MEDIUM: [https://medium.com/@ibraheemn13/ai-storyteller-2e9c940e17c7]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## AI Storyteller | Tools & Technology

* <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
* <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
* <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
* <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
* <img src="https://img.shields.io/badge/Whisper_AI-000000?style=for-the-badge&logo=openai&logoColor=white" />
* <img src="https://img.shields.io/badge/Google_Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white" />
* <img src="https://img.shields.io/badge/ElevenLabs-E63946?style=for-the-badge&logo=ai&logoColor=white" />
* <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" />

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## AI Storyteller | Installation & Running Locally

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/AI-StoryTeller.git
cd AI-StoryTeller
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
Create a `.env` file and add the following keys:
```sh
GEMINI_API_KEY=your_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### 5️⃣ Run the Backend Server
```sh
uvicorn main:app --reload
```
- The API runs at **`http://127.0.0.1:8000`**  
- Visit **`http://127.0.0.1:8000/docs`** for API testing  

### 6️⃣ Run the Frontend
Simply **open `index.html` in a browser**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## AI Storyteller | API Endpoints

| **Method** | **Endpoint** | **Description** |
|------------|-------------|----------------|
| `POST` | `/transcribe/` | Transcribes speech or accepts typed input |
| `POST` | `/generate_story/` | Uses Gemini AI to create a story |
| `POST` | `/generate_speech/` | Converts text to speech (ElevenLabs) |
| `GET` | `/get_audio` | Fetches generated audio for playback |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## AI Storyteller | Contributing

Contributions are what make open-source projects amazing! If you have suggestions to improve this project, feel free to fork the repo and submit a pull request.

1. Fork the Project
2. Create your Feature Branch `git checkout -b feature/AmazingFeature`
3. Commit your Changes `git commit -m 'Add some AmazingFeature'`
4. Push to the Branch `git push origin feature/AmazingFeature`
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## AI Storyteller | DEMO
[![Watch the Demo](https://img.youtube.com/vi/v7Tz4T-Tfqc/0.jpg)](https://youtu.be/v7Tz4T-Tfqc)

  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---
<p align="center"> © 2025 Muhammad Ibraheem Noor, All Rights Reserved. </p>
<p align="center">
https://github.com/Ibraheemn13
</p>
