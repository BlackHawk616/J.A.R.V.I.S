import speech_recognition as sr
import os
import time
import pyautogui
from time import sleep
import keyboard
import psutil
import platform
import subprocess

from speech_engine import speak

IS_MAC = platform.system() == "Darwin"
MOD = "command" if IS_MAC else "ctrl"


def _open_app(mac_app: str, win_path: str = "") -> None:
    if IS_MAC:
        subprocess.run(["open", "-a", mac_app], check=False)
        return
    if win_path:
        os.startfile(win_path)


def _close_app(mac_app: str, win_exe: str = "") -> None:
    if IS_MAC:
        subprocess.run(["osascript", "-e", f'tell application "{mac_app}" to quit'], check=False)
        return
    if win_exe:
        os.system(f"taskkill /f /im {win_exe}")

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
    keyboard.press_and_release(f'{MOD}+r')
    speak("Sir Refreshed this Tab")

def pcrefresh():
    keyboard.press('F5')
    speak("Sir Refreshed This Pc")

def savefile():
    speak('Ok Sir')
    keyboard.press_and_release(f'{MOD}+s')

def selectall():
    speak("Ok Sir")
    keyboard.press_and_release(f'{MOD}+a')

def copy():
    speak("OK Sir")
    keyboard.press_and_release(f'{MOD}+c')

def paste():
    speak("OK Sir")
    keyboard.press_and_release(f'{MOD}+v')

def taskmanager():
    speak("OK Sir")
    if IS_MAC:
        _open_app("Activity Monitor")
    else:
        keyboard.press_and_release('Ctrl + shift + Esc')

def close():
    speak("Ok Sir")
    if IS_MAC:
        keyboard.press_and_release('command+w')
    else:
        keyboard.press_and_release('Alt + F4')

def rename():
    speak("Ok Sir")
    keyboard.press('F2')

def newfolder():
    speak("Ok Sir")
    keyboard.press_and_release(f'{MOD}+shift+n')

def notepad():
    _open_app("TextEdit", "C:\\Windows\\system32\\notepad.exe")

def vlcmediaplayer():
    _open_app("VLC", "D:\\VLC\\vlc.exe")

def epicgamesstore():
    _open_app("Epic Games Launcher", "D:\\game devlopement\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")

def obsstudio():
    _open_app("OBS", "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe")

def blender():
    _open_app("Blender", "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe")

def tlauncher():
    _open_app("TLauncher", "C:\\Users\\USER\\AppData\\Roaming\\.minecraft\\TLauncher.exe")

def opera():
    _open_app("Opera", "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")

def  spotify():
    _open_app("Spotify", "C:\\Users\\opsri\\AppData\\Roaming\\Spotify\\Spotify.exe")

def open_virtual_box():

    speak("Ok Sir Opeing Virtual Box")

    _open_app("VirtualBox", "G:\\Apps\\Virtual Box\\VirtualBox.exe")

def open_discord():

    speak("Ok Sir Opeing Discord")

    _open_app("Discord", "C:\\Users\\opsri\\AppData\\Local\\Discord\\Update1.exe --processStart Discord.exe")

#def firefox():
    #jpath = 

def switchthewindow():
    speak("switching the window")
    pyautogui.keyDown("command" if IS_MAC else "alt")
    pyautogui.press("tab")
    sleep(1)
    pyautogui.keyUp("command" if IS_MAC else "alt")

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
    speak("ok Sir closing media player")
    _close_app("QuickTime Player", "wmplayer.exe")
    speak("Sir Closed media player")

def close_chrome():
    speak("Ok Sir, closing chrome")
    _close_app("Google Chrome", "chrome.exe")
    speak("Sir, Closed Chrome")

def close_opera():
    speak("Ok Sir, Closing opera browser")
    _close_app("Opera", "opera.exe")
    speak("Sir, Closed Opera")

def close_vscode():
    speak("Ok Sir, closing visual studio code")
    _close_app("Visual Studio Code", "code.exe")
    speak("Sir, Closed Visual Studio Code")

def close_discord():
    speak("Ok Sir, Closing Discord")
    _close_app("Discord", "discord.exe")
    speak("Sir, Closed Discord")

def close_aducaiy():
    speak("Ok Sir, Closing audacity")
    _close_app("Audacity", "audacity.exe")
    speak("Sir, Closed Audacity")

def close_firefox():
    speak("Ok Sir, Closing firefox")
    _close_app("Firefox", "firefox.exe")
    speak("Sir, Closed Fire fox")

def close_touchvpn():
    speak("ok Sir, Closing Touch vpn")
    _close_app("TouchVPN", "TouchVpn.exe")
    speak("Sir, closed Touch Vpn")

def close_blender():
    speak("Ok Sir, Closing Blender 3d Softare")
    _close_app("Blender", "blender.exe")
    speak("Sir, Closed Blender")

def close_tlauncher():
    speak("Ok Sir, Closing Tlauncher")
    _close_app("TLauncher", "java.exe")
    speak("Sir, Closed Tlauncher")

def close_minecraft():
    speak("Ok Sir, Closing minecraft")
    _close_app("Minecraft", "minecraft.exe")
    speak("Sir, Closed Minecraft")

def close_d3dgear():
    speak("Ok Sir, Closing D3Dgear")
    _close_app("D3Dgear", "d3dgear.exe")
    speak("Sir, Closed D3DGEAR")

def close_vlcmediaplayer():
    speak("Ok Sir, Closing vlc media player")
    _close_app("VLC", "vlc.exe")
    speak("Sir, closed vlc media player")
        
def close_this_file():
    speak("Ok Sir, closing This program")
    if IS_MAC:
        keyboard.press_and_release('command+w')
    else:
        keyboard.press('Alt + F4')
    sleep(2)
    speak("Sir, Closed The Program")