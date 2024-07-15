import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import keyboard
from pyautogui import click
from time import sleep
import mouse
from pywhatkit import sc

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

def google_search():

    query = take_command().lower()     

    speak("This Is What I Found For Your Search Sir!")
    query = query.replace("search in","")
    query = query.replace("google","")
    kit.search(query)
    speak("Done Sir!")

def history():

    speak("Ok Sir, opning history in opera")
    keyboard.press('CTRL+H')
    speak("Sir, opened history in opera")

def downloads():

    speak("Ok Sir, opening downloads in chrome")
    keyboard.press('CTRL + J')
    speak("Sir, opened downloads in chrome")    

def new_tab():

    speak("Ok Sir, opening new tab in chrome")
    keyboard.press('Ctrl + n')
    speak("Sir opened new tab")

def new_window_in_incognito_mode():

    speak("Ok Sir opening new window in Incognito mode")
    keyboard.press('Ctrl + Shift + n')
    speak("Sir, opened new window in Incognito mode")

def switch_workspaces():
    speak("OK Sir Switching Work Space")
    click()
    sleep(2)
    speak("Sir, switched Workspace")

def switch_Tab():
    
    speak("Ok Sir Switching The Tab")
    keyboard.press_and_release('Alt + Tab')
    speak("Sir switched Tab")

def enable_vpn():

    speak("Ok Sir Enabling Vpn")
    
    sleep(2)
    
    click()
    
    sleep(2)

    speak("Sir Which Location Shall I Select")

    query = take_command().lower()

    if " select Europe" in query:

        speak("Ok Sir Connecting To Europe's Server")

        click()

        speak("Sir Connected To Europe")

    elif " select america" in query:

        speak("Ok Sir Connecting To America's Server")

        click()

        speak("Sir Connected To America")

    elif " select asia" in query:

        speak("Ok Sir Connecting Asia's Server ")

        click()

        speak("Sir Connected To Asia")

    else:
        speak("Due To Some Errors Unable To Switch")

def disable_darkpage():

    speak("Ok Sir Disabling Force Dark Page On This Website")

    click()

    mouse.click('right')

    click()

    speak("Sir Disabled forced Darkpage")

def close_this_tab():

    speak("Ok Sir, closing This Tab")
    
    keyboard.press("CTRL + Tab")

    speak("sir Closed This Tab")

