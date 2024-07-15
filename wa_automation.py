from email.mime import audio
from time import sleep
from pyautogui import doubleClick
import pyttsx3
import speech_recognition as sr
import keyboard
from pyautogui import click

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
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


def wa_automation_for_msg():

    speak("OK Sir Opening whatsapp")

    doubleClick(x=611, y=753)

    sleep(2)

    doubleClick(x=188, y=112)

    sleep(2)

    speak("Sir Whom Should I Send The Message")

    name = takecommand()

    keyboard.write(name)

    speak(f"Whatsapp User Name:- {name}\n")

    speak("searching User") 
   
    speak("User Found Sir")

    click(x=197, y=181)

    sleep(2)

    click(x=635, y=734)

    speak("Sir What Is The Message")

    msg = takecommand().lower()

    keyboard.write(msg)

    speak(f"Sir This The Message You Told Me To Send {msg}\n")
    
    speak("sir Shall I Send The Message")

    query = takecommand().lower()


    if " yes send the message" in query:

        speak("Ok Sir sending Message")

        click(x=1344, y=708)

        sleep(2)

        speak(f"Sir Sent The Message to {name}\n")

    elif " no dont send the message" in query:

        speak("Ok sir Not Sending The Message")

    else:
        speak("Sorry sir Unable To Understand")

def call_():

    #Replacces The Command
    query = takecommand().lower()
    query = query.replace("ulron","")
    query = query.replace("call","")

    speak(f"Ok Sir Calling{query}\n")

    #opens Whatsapp       
    click(x=611, y=753)

    sleep(2)

    #Clicks On Search
    click(x=188, y=112)

    sleep(2)

    #It Writes The Username To Call
    keyboard.write(query)

    #Click On That User
    click(x=197, y=181)

    sleep(2)

    speak("Sir Shall I voice call, or Video Call")

    if " voice call" in query:

        speak(f"Ok Sir Voice Calling{query}\n")

        click()

        sleep(3)

        speak(f"Sir Voice Calling{query}\n")

    elif " video call" in query:

        speak(f"Ok Sir Video Calling{query}\n")

        click()

        sleep(2)

        speak(f"Sir Video Calling{query}\n")

    else:
        speak("Sorry Sir Unable To Call")

def demo():

    query = takecommand().lower()

    if " hello ultron" in query:

        speak("Hello Sir")

    elif " call " in query:

        speak("OK")
        call_()
    
    else:

        speak("Sorry Sir")

demo()