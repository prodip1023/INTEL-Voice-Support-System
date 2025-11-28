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
load_dotenv()
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

# #########################################################
# 7. Greeting the user
# #########################################################
def greet_user():
    """
    This function is used to greet the user
    Args:
        None
    Returns:
        None
    """
    speak("Hello, I am an AI Assistant")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir! How are you doing?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
    
    speak("I am an AI Assistant, how can I help you today?")

def play_music():
    music_dir = "F:\\Assignment-JARVIS-System\\music"
    try:
        songs = os.listdir(music_dir)

        if songs:
            random_song = random.choice(songs)
            speak(f"Playing a random song sir: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))
            logging.info(f"Playing music: {random_song}")
        else:
            speak("No music files found in your music directory.")

    except Exception as e:
        logging.error(f"Error in play_music: {e}")
        speak("Sorry sir, I could not find your music folder.")

        
# #########################################################
# 8. Using Generative Model 
# #########################################################
def generaive_response(user_input):
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    # user_input = "what is python"
    prompt = f"Your name is AI Assistant, You act like AI Assistance, Please provide a short answer in my Qustions:{user_input}"
    response = model.generate_content(prompt)
    result = response.text
    return result
 


greet_user()




while True:
    query = takeCommand().lower()
    # print(query)
    if "your name" in query:
        speak("I am an AI Assistant")
        logging.info("User asked about name")
    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
        logging.info(f"The time is {time}")
    elif "who made you" in query:
        speak("I was created by Prodip Sarkar.")
        logging.info("User asked about assistant's creator.")
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")
    elif "open google" in query:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
        logging.info("User asked to open Google.")
    elif "open youtube" in query:
        speak("Opening YouTube for you.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("User requested to search on YouTube.")
    elif "open linkedin" in query:
        speak("Opening Linkedin...")
        webbrowser.open("https://www.linkedin.com/")
        logging.info("User asked to open Linkedin.")
    elif "open calender" in query or "google calender":
        speak("Opening Google Calender")
        webbrowser.open("https://calendar.google.com/")
        logging.info("User asked to open Google Calender.")
    elif "open facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("facebook.com")
        logging.info("User requested to open Facebook.")
    
    elif "open github" in query:
        speak("ok sir. opening github")
        webbrowser.open("github.com")
        logging.info("User requested to open GitHub.")
    # open wikipedia
    elif "open wikipedia" in query or "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentence=2)
        speak("According to wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")

    # Open calculator
    elif "open calculator" in query or "calculator" in query:
        speak("Opening Calculator...")
        subprocess.Popen("calc.exe")
        logging.info("User asked to open Calculator.")
    # Open notepad
    elif "open notepad" in query or "notepad" in query:
        speak("Opening Notepad...")
        subprocess.Popen("notepad.exe")
        logging.info("User asked to open Notepad.") 
    # Open Terminal
    elif "open terminal" in query or "open command prompt" in query:
        speak("Opening Command Prompt...")
        subprocess.Popen("cmd.exe")
        logging.info("User asked to open Terminal.") 
    # Open System Calender
    elif "system calender" in query :
        speak("Opening System Calender...")
        subprocess.Popen(["start", "ms-calendar:"], shell=True)
        logging.info("User asked to open System Calender.") 
    
    # random jokes choice
    elif "jokes" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said no problem, it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))
        logging.info("User requested a joke.")
    
    elif "play music" in query or "music" in query:
        play_music()
    
    elif "exit" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

    else:
        response = generaive_response(query)
        speak(response)
        logging.info("User asked for others question")
        # speak("I am sorry, I am not able to understand you")
        # logging.error("User asked about name")

   