import pyttsx3
import speech_recognition as sr
import requests
import webbrowser
from pyautogui import click
from time import sleep
import keyboard


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,  language='en=in')
        print(f"Sir Ram said: {query}\n")

    except Exception as e:
        #print(e)
        print("Sir Please say that again please")
        speak("Sir Please say that again please")
        return "none"
    return query

def youtube_search():

    query = takecommand().lower()

    speak("OK Sir , This Is What I found For Your Search!")
    query = query.replace("Search","")
    query = query.replace("In","")
    query = query.replace("youtube","")
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(web)
    speak("Done Sir!")

def pause_video():
    speak("Ok Sir, I am Pausing video")
    keyboard.press('SPACE')
    speak("Sir video paused")

def resume_video():
    speak("Ok Sir, I am resumeing video")
    keyboard.press('SPACE')
    speak("Sir, video resumed")

def skip_10_seconds_forward():
    speak("OK Sir, Skiping the video ten seconds forward")
    keyboard.press('L')
    speak("Sir, I had skipped the video 10 seconds forward")    

def rewind_10_seconds_back():
    speak("ok Sir, i am rewinding the video")
    keyboard.press('J')
    speak("Sir, video rewinded")

def skip_ad():
    speak("Wait Sir, i am Skipping the add")
    click(x=830, y=535)
    speak("Sir, i had skipped the video")   

def like_video():
    speak("Wait Sir, I am liking")
    click(x=473, y=704)
    speak("Sir, I liked the video")

def fullscreen():
    speak("Ok Sir, playing video in full screen")
    keyboard.press('F')
    speak("Sir, done")

def therather_mode():
    speak("Ok Sir, playing video in thearther mode")
    keyboard.press('T')
    speak("Sir, Done")
