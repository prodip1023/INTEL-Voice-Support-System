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
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Logging started")

# #########################################################
# 4. Activating voice from the system
# #########################################################

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)



