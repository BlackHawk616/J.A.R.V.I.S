import speech_recognition as sr
import pyttsx3
import os
import time
import pyautogui
from time import sleep
import keyboard
import psutil

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

def ram_usage():

    pc_ram_usage = str(psutil.virtual_memory()[2])

    speak("Sir Current Ram Usage is " + pc_ram_usage)

    print("Sir Current Ram Usage Is " + pc_ram_usage) 

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Sir CPU usage is at " + usage)
    print("CPU usage is at " + usage)

def refresh():
    keyboard.press_and_release('ctrl + r')
    speak("Sir Refreshed this Tab")

def pcrefresh():
    keyboard.press('F5')
    speak("Sir Refreshed This Pc")

def savefile():
    speak('Ok Sir')
    keyboard.press_and_release('ctrl + s')

def selectall():
    speak("Ok Sir")
    keyboard.press_and_release('ctrl + A')

def copy():
    speak("OK Sir")
    keyboard.press_and_release('ctrl + C')

def paste():
    speak("OK Sir")
    keyboard.press_and_release('ctrl + V')

def taskmanager():
    speak("OK Sir")
    keyboard.press_and_release('Ctrl + shift + Esc')

def close():
    speak("Ok Sir")
    keyboard.press_and_release('Alt + F4')

def rename():
    speak("Ok Sir")
    keyboard.press('F2')

def newfolder():
    speak("Ok Sir")
    keyboard.press('ctrl + Shift + N')

def notepad():
    apath = "C:\\Windows\\system32\\notepad.exe"
    os.startfile(apath)

def vlcmediaplayer():
    dpath = "D:\\VLC\\vlc.exe"
    os.startfile(dpath)

def epicgamesstore():
    epath = "D:\\game devlopement\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
    os.startfile(epath)

def obsstudio():
    fpath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
    os.startfile(fpath)

def blender():
    gpath = "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe"   
    os.startfile(gpath) 

def tlauncher():
    hpath = "C:\\Users\\USER\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
    os.startfile(hpath)

def opera():
    ipath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
    os.startfile(ipath)

def  spotify():
    jpath = "C:\\Users\\opsri\\AppData\\Roaming\\Spotify\\Spotify.exe"
    os.startfile(jpath)

def open_virtual_box():

    speak("Ok Sir Opeing Virtual Box")

    kpath = "G:\\Apps\\Virtual Box\\VirtualBox.exe"

    os.startfile(kpath)

def open_discord():

    speak("Ok Sir Opeing Discord")

    lpath = "C:\\Users\\opsri\\AppData\\Local\\Discord\\Update1.exe --processStart Discord.exe"

    os.startfile(lpath)

#def firefox():
    #jpath = 

def switchthewindow():
    speak("switching the window")
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    sleep(1)
    pyautogui.keyUp("alt")

def volume_up():
    pyautogui.press("volumeup")
    speak("Sir,i had increased the volume")    

def volume_down():
    pyautogui.press("volumedown")
    speak("Sir,I had Decreased the volume")

def mute_audio():
    speak("yes sir i can mute the audio")
    speak("Sir i had muted the audio")
    pyautogui.press("volumemute")

def unmute_audio():
    pyautogui.press("volumemute")
    sleep(3)
    speak("Sir Audio unmuted")

def close_windowsmediaplayer():
    speak("ok Sir closing windows media player")
    os.system("taskkill /f /im wmplayer.exe")
    speak("Sir Closed Windows media player")

def close_chrome():
    speak("Ok Sir, closing chrome")
    os.system("taskkill /f /im chrome.exe")
    speak("Sir, Closed Chrome")

def close_opera():
    speak("Ok Sir, Closing opera browser")
    os.system("taskkill /f /im opera.exe")
    speak("Sir, Closed Opera")

def close_vscode():
    speak("Ok Sir, closing visual studio code")
    os.system("taskkill /f /im code.exe")
    speak("Sir, Closed Visual Studio Code")

def close_discord():
    speak("Ok Sir, Closing Discord")
    os.system("taskkill /f /im discord.exe")
    speak("Sir, Closed Discord")

def close_aducaiy():
    speak("Ok Sir, Closing audacity")
    os.system("taskkill /f /im audacity.exe")
    speak("Sir, Closed Audacity")

def close_firefox():
    speak("Ok Sir, Closing firefox")
    os.system("taskkil /f /im firefox.exe")
    speak("Sir, Closed Fire fox")

def close_touchvpn():
    speak("ok Sir, Closing Touch vpn")
    os.system("taskkill /f /im TouchVpn.exe")
    speak("Sir, closed Touch Vpn")

def close_blender():
    speak("Ok Sir, Closing Blender 3d Softare")
    os.system("taskkill /f /im blender.exe")
    speak("Sir, Closed Blender")

def close_tlauncher():
    speak("Ok Sir, Closing Tlauncher")
    os.system("taskkill /f /im java.exe")
    speak("Sir, Closed Tlauncher")

def close_minecraft():
    speak("Ok Sir, Closing minecraft")
    os.system("taskkill /f /im minecraft.exe")
    speak("Sir, Closed Minecraft")

def close_d3dgear():
    speak("Ok Sir, Closing D3Dgear")
    os.system("taskkill /f /im d3dgear.exe")
    speak("Sir, Closed D3DGEAR")

def close_vlcmediaplayer():
    speak("Ok Sir, Closing vlc media player")
    os.system("taskkill /f /im vlc.exe")
    speak("Sir, closed vlc media player")
        
def close_this_file():
    speak("Ok Sir, closing This program")
    keyboard.press('Alt + F4')
    sleep(2)
    speak("Sir, Closed The Program")