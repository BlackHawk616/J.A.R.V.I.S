import datetime
import os
import platform
import subprocess
from calendar import month
from time import sleep

import pyjokes
import pyscreeze
import speech_recognition as sr
from pyautogui import click
from pywikihow import search_wikihow
from speech_engine import speak
from memory import add_memory

# Take Command Engine

def take_command():
    r = sr.Recognizer()

    # ── Tune sensitivity so ambient noise is ignored ────────────
    r.energy_threshold = int(os.environ.get("JARVIS_SR_ENERGY", "4000"))
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8          # seconds of silence before phrase ends

    with sr.Microphone() as source:
        # Calibrate to current background noise level
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return "none"

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print(f"User Said : {query}\n")

        # Discard garbage / very short recognitions
        if len(query.strip()) < 2:
            return "none"

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

    speak(j, blocking=False)

def hide():
    if platform.system() == "Darwin":
        subprocess.run("find . -maxdepth 1 -mindepth 1 -exec chflags hidden {} +", shell=True, check=False)
    else:
        os.system("attrib +h /s /d")

    speak("Sir All Files Are Hidden Now")

def unhide():
    if platform.system() == "Darwin":
        subprocess.run("find . -maxdepth 1 -mindepth 1 -exec chflags nohidden {} +", shell=True, check=False)
    else:
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

    if d2ata and d2ata != "none":
        speak("Sir, You Said To Remember That " + d2ata)
        bullet = add_memory(d2ata)
        speak("Stored in my memory Sir.")
        print(f"[Memory] {bullet}")
    else:
        speak("I didn't catch that Sir.")

def introuce():

    speak("Hello I Am Jarvis, A Vritual AI")
    speak("I Am Here To Help Assist You In Your Work")
    speak("My Main Functions Are, To Protect You, And Help You To achieve Your Goals ,And Task")