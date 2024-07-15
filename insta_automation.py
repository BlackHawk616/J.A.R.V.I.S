import pyttsx3
import speech_recognition as sr
from pyautogui import click
from time import sleep
import keyboard 
from keyboard import write

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

        print("Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recongnizing...")

        query = r.recognize_google(audio, language='en-in')

        print(f"User Said: {query}\n")

    except Exception as e:

        print("Sir Please Say That Again please")

        speak("Sir Please Say That Again")

        return "none"

    return query

def open_ig():

    speak("Ok Sir Opening Instagram")

    # Instagram Opening

    click()
    
    click()

    sleep(5)

    speak("Sir Opened Instagram")

def open_my_pf():

    speak("Ok Sir Opeing Your Profile")
 
    # Instagram Opening
    
    click()
    
    click()

    sleep(2)

    click()

    speak("Sir Opened Your Profile")

def open_chat():

    speak("Ok Sir Opening Chats")

    click()

    speak("Sir Opened Chats")

def send_msg():

    click()

    speak("Sir Please Tell Me The Message")

    msg_1 = takecommand()

    keyboard.write(msg_1)

    speak(f"sir You Said : {msg_1}\n")

    sleep(2)

    click()

    sleep(2)

    speak("Sir Message Had Been Sent")



    



     




