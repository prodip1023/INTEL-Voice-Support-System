# #########################################################
# 1. Importing Libraries
# #########################################################

import speech_recognition as sr
import pyttsx3
import wikipedia
import google.generativeai as genai
import os
from dotenv import load_dotenv
import datetime
import logging
import webbrowser
import random 
import subprocess 

# #########################################################
# 2. Setting up the Environment
# #########################################################

google_api_key = os.getenv("GOOGLE_API_KEY")

# #########################################################
# 3. Setting up the Logging
# #########################################################
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_NAME = "jarvis.log"
log_file_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
logging.info("Logging started")

# #########################################################
# 4. Activating voice from the system
# #########################################################

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170) # 170 is the speed of the voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# #########################################################
# 5. Creating a function to speak
# #########################################################
def speak(text):
    """
    This function is used to speak the text
    Args:
        text (str): The text to speak
    Returns:
      voice
    """
    engine.say(text)
    engine.runAndWait()
    logging.info(f"Speaking: {text}")


# #########################################################
# 6. Creating a function to take command from the user
# #########################################################
def takeCommand():
    """
    This function is used to take command from the user
    Args:
        None
    Returns:
        command (str): The command to execute
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        logging.info("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        logging.info(f"User said: {query}")
        
    
    except Exception as e:
        print("Say that again please...")
        logging.error(f"Error: {e}")
        return "None"

    return query

query = takeCommand()
print(query)