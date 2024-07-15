from time import sleep
import pyttsx3
import speech_recognition as sr
from pyautogui import click, scroll

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[5].id)
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

def mute():

    speak("Ok Sir Muting Mic") 

    click()

    sleep(2)

    speak("Sir Mic Is Muted")

def unmute():

    speak("Ok Sir Unmuting Mic")

    click()

    sleep(2)

    speak("Sir Mic Is Unmuted")

def Defean():

    speak("ok Sir Defeaning")

    click()

    sleep(2)

    speak("Sir Defeaned")

def undefean():

    speak("Ok Sir Un defeaning")

    click()

    sleep(2)

    click("Ok Sir Undefeaned")

def disconnect():

    speak("Ok Sir Leaving The Call")

    click()

    sleep(2)

    speak("Sir Leaved The Call")

def call_Him():

    query = takecommand.lower()

    speak("Sir Shall I Voice call Him Or Video call")

    sleep(2)

    if " voice call" in query:

        speak("Ok Sir Call Him")

        click()

        sleep(2)

        speak("sir Calling Him")

    elif " video call" in query:

        speak("Ok Sir Calling Him")
        
        sleep(2)

        click()
        
        speak("Sir Calling Him")

    else:
        speak("Sorry Sir Unable To Call Him")


def stop_screenshare():

    speak("Ok Sir Stoping Screen Share")

    click()

    sleep(2)

    speak("Sir Stopped Screen share")


 

    