import speech_recognition as sr
import pywhatkit as kit
import keyboard
import platform
from pyautogui import click
from time import sleep
from pywhatkit import sc
from speech_engine import speak

try:
    import mouse
except Exception:
    mouse = None

MOD = "command" if platform.system() == "Darwin" else "ctrl"

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
    keyboard.press_and_release(f'{MOD}+h')
    speak("Sir, opened history in opera")

def downloads():

    speak("Ok Sir, opening downloads in chrome")
    keyboard.press_and_release(f'{MOD}+j')
    speak("Sir, opened downloads in chrome")    

def new_tab():

    speak("Ok Sir, opening new tab in chrome")
    keyboard.press_and_release(f'{MOD}+n')
    speak("Sir opened new tab")

def new_window_in_incognito_mode():

    speak("Ok Sir opening new window in Incognito mode")
    keyboard.press_and_release(f'{MOD}+shift+n')
    speak("Sir, opened new window in Incognito mode")

def switch_workspaces():
    speak("OK Sir Switching Work Space")
    click()
    sleep(2)
    speak("Sir, switched Workspace")

def switch_Tab():
    
    speak("Ok Sir Switching The Tab")
    if platform.system() == "Darwin":
        keyboard.press_and_release('command+tab')
    else:
        keyboard.press_and_release('alt+tab')
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

    if mouse is not None:
        mouse.click('right')

    click()

    speak("Sir Disabled forced Darkpage")

def close_this_tab():

    speak("Ok Sir, closing This Tab")
    
    keyboard.press_and_release(f'{MOD}+w')

    speak("sir Closed This Tab")

