# INTEL-Voice-Support-System

A smart AI voice assistant designed to help users perform tasks using voice commands.
It works like a personal AI helper that listens, understands, and responds.

# 🛠️ Features:-
- Opening websites
- Opening Wikipedia
- Opening files/programs
- Giving answers
- Searching Google/Wikipedia
- Open system applications: Calculator, Notepad, CMD
- Open Calendar (Google Calendar via browser)
- Open Camera and capture image (new feature)
- Play random music
- Exit gracefully with a voice command
- Using "Generative AI" model - gemini-2.5-flash

# 💻 Requirements :
Python 3.11 + 

# How to run?
1. Create Environment
```bash
conda create -n jarvis python==3.11 -y
```
2. Activate Environment
```bash
conda activate jarvis
```
3. Create requirements.txt for installing required packages
```bash
pip install -r requirements.txt
```
4. Create Google API Key and store .env file because of hidden key.
5. Run the JARVIS script
```bash
python jarvis.py
```
# Folder Structure
```
INTEL-Voice-Support-System/
├── music/
│   ├── 1
│   ├── 2
│   └── 3
├── .env
├── .gitignore
├── README.md
├── LICENSE
├── jarvis.py
├── requirements.txt
└── test.ipynb
```

#  Demo Video
[![Watch the video](assets/Capture.png)](https://drive.google.com/file/d/1rfUzb0P3t0Z_6gA7S4xqD-Kt9dr1oYVY/view?usp=drive_link)

# Reference 
- https://pypi.org/project/SpeechRecognition/3.14.3/
- https://pypi.org/project/pyttsx3/2.90/
- https://pypi.org/project/PyAudio/0.2.14/
- https://pypi.org/project/wikipedia/1.4.0/
- https://pypi.org/project/google-generativeai/0.8.4/
- https://aistudio.google.com/api-keys
- https://pypi.org/project/python-dotenv/1.2.1/
- https://docs.python.org/3/library/logging.html
- https://tree.nathanfriend.com/

# 👨‍💻 Author
<b>Prodip Sarkar</b>

Linkedin - https://www.linkedin.com/in/prodip1023/

# 📜 License
This project is open-source and free to use for learning purposes.


