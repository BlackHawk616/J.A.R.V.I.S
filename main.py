import datetime
import os
from calendar import month
from time import sleep

import pyjokes
import pyscreeze
import pyttsx3
import speech_recognition as sr
from pyautogui import click
from pywikihow import search_wikihow

# Voice Engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Take Command Engine

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en=us')
        print(f"Use Said : {query}\n")

    except Exception as e:
        #print(e)
        print("Sir Please Say That Again Please")
        speak("Sir Please Say That Again Please")
        return "none"

    return query

def WishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour>=12:
        speak("Good Morning Sir")
        speak("All features imported Sucessfully")

    elif hour>=12 and hour>=18:
        speak("Good Afternoon Sir")
        speak("All features imported Sucessfully")

    else:
        speak("Its evening Sir")
        speak("All features imported Sucessfully")


def screenshot(): # Done
    speak("Sir tell me what name should i give for the screenshot")
    
    name = take_command()
    
    speak("please boss hold the screen for few seconds,i am taking screen shot")
    
    sleep(3)
    
    img = pyscreeze.screenshot()
    
    img.save(f"{name}.png")
    
    speak("Sir i took the screen shot")

def date():
    
    year = int(datetime.datetime.now().year)
    
    month = int(datetime.datetime.now().month)
    
    date = int(datetime.datetime.now().day)
    
    speak("Sir, The Current Date Is")
    
    speak(date)

    speak(month)

    speak(year)

def time():

    Time = datetime.datetime.now().strftime("%H:%M")

    speak("Sir The Current Time Is")

    speak(Time)

def jokes():

    j = pyjokes.get_joke()
    
    print(j)

    speak(j)

def hide():

    os.system("attrib +h /s /d")

    speak("Sir All Files Are Hidden Now")

def unhide():

    os.system("attrib -h /s /d")

    speak("All Files Are Visible Sir")

def activate_how_to_do_mode():

    speak("Sir Activated How To Do Mode")

    how = take_command()

    max_results = 1

    how_to = search_wikihow(how, max_results)

    assert len(how_to) == 1

    how_to[0].print()

    speak(how_to[0].summary)

def reminder_maker():

    speak("Sir What is the remainder?")

    d2ata = take_command()

    speak("Sir, You Said To Remember That" + d2ata)  # type: ignore

    reminder_file = open("data.txt", 'a')

    reminder_file.write('\n')

    reminder_file.write(d2ata)  # type: ignore

    reminder_file.close()

def introuce():

    speak("Hello I Am Jarvis, A Vritual AI")
    speak("I Am Here To Help Assist You In Your Work")
    speak("My Main Functions Are, To Protect You, And Help You To achieve Your Goals ,And Task")