from multiprocessing.spawn import old_main_modules
from tkinter import E
from turtle import shape
from unittest import skip
import speech_recognition as sr
import wikipedia
import time
from time import sleep
import pywhatkit as kit
import os
from nim_client import get_nim_response
from speech_engine import speak, stop_speaking, continue_speaking, should_ignore_query
from memory import init_memory, add_memory, search_memory, get_memory_context, get_all_memories, extract_remember_payload

#Youtube Automation

from yt_automate import youtube_search
from yt_automate import pause_video
from yt_automate import resume_video
from yt_automate import skip_10_seconds_forward
from yt_automate import rewind_10_seconds_back
from yt_automate import skip_ad
from yt_automate import like_video
from yt_automate import fullscreen
from yt_automate import therather_mode

#Pc Automation

from pcautomati0n import blender, close, close_blender, close_chrome, close_discord, close_firefox, close_minecraft, close_opera, close_this_file, close_tlauncher, close_vlcmediaplayer, close_vscode, close_windowsmediaplayer, copy, cpu, epicgamesstore, mute_audio, newfolder, notepad, obsstudio, opera, paste, ram_usage, refresh, rename, savefile, selectall, spotify, switchthewindow, taskmanager, tlauncher, unmute_audio, vlcmediaplayer, volume_down, volume_up

#opera Automation

from opera_automation import google_search
from opera_automation import history
from opera_automation import downloads
from opera_automation import new_tab
from opera_automation import new_window_in_incognito_mode
from opera_automation import switch_workspaces
from opera_automation import switch_Tab
from opera_automation import enable_vpn
from opera_automation import disable_darkpage
from opera_automation import close_this_tab

# Music 

from music import Bad_liar, me_my_self
from music import heat_waves
from music import infinity
from music import stereo_hearts
from music import night_changes
from music import unstoppable
from music import love
from music import Old_Town_Road
from music import begging
from music import Let_Me_Down
from music import In_The_Middle_OF_The_Night
from music import A_Man_Without_Love
from music import startboy_weekend_draft
from music import ture_love
from music import Copy
from music import hoes_no_jujustu
from music import Bad_liar
from music import arcade
from music import idfc
from music import Shape_OF_You
from music import industry
from music import blinding_lights
from music import One_Dance
from music import Billie_eiliesh
from music import One_Kiss
from music import Play_My_Playlist

# Space Exp

# from nasa import Space_Info
# from nasa import IssTracker

#Main 

from main import WishMe
from main import screenshot
from main import date
from main import time
from main import jokes
from main import hide
from main import unhide
from main import activate_how_to_do_mode
from main import reminder_maker

#weather
from weather import weather

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


def TaskeExecution():

    # ── Load persistent memory from vector DB ───────────────
    init_memory()

    WishMe()

    date()

    time()

    while True:

        query = take_command().lower()

        # Skip processing if recognition failed or timed out
        if query == "none":
            continue

        # Ignore echo of our own voice
        if should_ignore_query(query):
            continue

        # If we got a valid command, stop any active speech immediately
        stop_speaking()

        # Handle explicit stop and continue commands
        if "stop" in query or "pause" in query:
            # We already stopped speaking via stop_speaking(), just acknowledge it
            speak("Stopped.")
            continue

        if "continue" in query or "resume" in query:
            if not continue_speaking():
                speak("Nothing to continue.")
            continue

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
        
            speak('Searching Wikipedia...')
        
            query = query.replace("wikipedia", "")
        
            results = wikipedia.summary(query, sentences=2) 
        
            speak("According to Wikipedia")
        
            print(results)
        
            speak(results, blocking=False)

            # Music

        elif "play me my self and i" in query:
                
            speak("OK Sir")

            me_my_self()

        elif "play heat waves" in query:
            
            speak("Ok Sir")

            heat_waves()

        elif "play infinity" in query:

            speak("Ok Sir")

            infinity()

        elif "play stereo hearts" in query:

            speak("Ok Sir")

            stereo_hearts()

        elif "play night changes" in query:

            speak("Ok Sir")

            night_changes()

        elif "play unstoppable" in query:

            speak("Ok Sir")

            unstoppable()

        elif "play love" in query:

            speak("ok Sir")

            love()
        
        elif "play old town road" in query:

            speak("Ok Sir")

            Old_Town_Road()

        elif "play begging" in query:

            speak("Ok Sir")

            begging()

        elif "play let me down" in query:

            speak("Ok Sir")

            Let_Me_Down()

        elif "play in the middle of the night" in query:

            speak("Ok Sir")

            In_The_Middle_OF_The_Night()

        elif "play a man without love" in query:

            speak("Ok Sir")

            A_Man_Without_Love()

        elif "play weekend" in query:

            speak("Ok Sir")

            startboy_weekend_draft()

        elif "play ture love" in query:

            speak("Ok Sir")

            ture_love()

        elif "play copy" in query:

            speak("Ok Sir")

            Copy()

        elif "in youtube" in query:

            speak("OK Sir")

            hoes_no_jujustu()

        elif "play bad liar" in query:

            speak("Ok Sir")

            Bad_liar()
        
        elif "play arcade" in query:

            speak("Ok Sir")

            arcade()

        elif "play shape of you" in query:

            speak("Ok Sir")

            Shape_OF_You()

        elif "play blinding lights" in query:

            speak("Ok Sir")

            blinding_lights()

        elif "play one dance" in query:

            speak("Ok Sir")

            One_Dance()

        elif "playing billie eilliesh" in query:

            speak("Ok Sir")

            Billie_eiliesh()

        elif "play one kiss" in query:

            speak("Ok Sir")

            One_Kiss()

        elif "play i dont care" in query:

            speak("Ok Sir")

            idfc()

        elif "play my playlist in spotify" in query:

            speak("starting spotify playlist automation")

            sleep(2)

            speak("Activated spotify playlist automation")

            Play_My_Playlist()


        # Youtube Automation

        elif "search in youtube" in query:

            youtube_search()

        elif "pause video" in query:

            pause_video()
        
        elif "resume video" in query:

            resume_video()

        elif "skip 10 seconds forward" in query:

            skip_10_seconds_forward()

        elif "rewind 10 seconds back" in query:

            rewind_10_seconds_back()

        elif "skip add" in query:

            skip_ad()

        elif "like video" in query:

            like_video()

        elif "fullscreen mode" in query:

            fullscreen()

        elif "therather mode" in query:

            therather_mode()

        elif "tell me a joke" in query:

            speak("Ok Sir, Please Wait I am Finding A joke For You")

            jokes()

        elif "hide your files" in query:

            speak("Ok Sir, Hiding My Files")

            hide()

        elif "unhide your files" in query:

            speak("Ok Sir, Unhiding My files")

        elif "turn on how to do" in query:

            speak("Ok Sir")

            activate_how_to_do_mode()

        elif "what do you remember" in query:

            memories = get_all_memories()
            if memories:
                speak(f"Sir, I have {len(memories)} things in my memory.")
                for mem in memories[:5]:  # Read at most 5 aloud
                    print(mem)
                    speak(mem)
                if len(memories) > 5:
                    speak(f"And {len(memories) - 5} more memories stored.")
            else:
                speak("My memory is empty Sir. Tell me to remember something.")

        elif "remember" in query:

            payload = extract_remember_payload(query)
            if payload:
                bullet = add_memory(payload)
                speak("Got it Sir. I will remember that.")
                print(f"[Memory] {bullet}")
            else:
                speak("Sir, what should I remember?")
                mem_data = take_command()
                if mem_data != "none":
                    bullet = add_memory(mem_data)
                    speak("Got it Sir. I will remember that.")
                    print(f"[Memory] {bullet}")
                else:
                    speak("I didn't catch that Sir.")

        elif "take screenshot" in query:

            screenshot()

        # Pc Automation

        elif "what is the ram usage" in query:

            ram_usage()

        elif "what is the cpu usage" in query:

            cpu()

        elif "refresh this tab" in query:

            refresh()

        elif "save this file" in query:

            savefile()

        elif "select all" in query:

            selectall()

        elif "copy this" in query:

            copy()

        elif "paste it here" in query:

            paste()

        elif "open taskmanager" in query:

            taskmanager()

        elif "close this" in query:

            close()

        elif "rename this" in query:

            rename()

        elif "make a new folder here" in query:

            newfolder()

        elif "open notepad" in query:

                notepad()

        elif "open vlc media player" in query:

            vlcmediaplayer()

        elif "open epic games store" in query:

            epicgamesstore()

        elif "open obs studio" in query:

            obsstudio()

        elif "open blender" in query:

            blender()

        elif "open tlauncher" in query:

            tlauncher()

        elif "open opera" in query:

            opera()

        elif "open spotify" in query:

            spotify()

        elif "switch the window" in query:

            switchthewindow()

        elif "increase volume" in query:

            volume_up()

        elif "decrease volume" in query:
            
            volume_down()

        elif "mute audio" in query:

            mute_audio()
        
        elif "unmute audio" in query:

            unmute_audio()

        elif "close windows media player" in query:

            close_windowsmediaplayer()

        elif "close chrome" in query:

            close_chrome()

        elif "close opera" in query:

            close_opera()

        elif "close visual code" in query:

            close_vscode()
        
        elif "close discord" in query:

            close_discord()

        elif "close fire fox" in query:

            close_firefox()

        elif "close bleneder" in query:

            close_blender()
        
        elif "close t launcher" in query:

            close_tlauncher()

        elif "close minecraft" in query:

            close_minecraft()

        elif "close vlc media player" in query:

            close_vlcmediaplayer()

        elif "close this" in query:

            close_this_file()

        elif "what is the weather forecast" in query:

            weather()

        elif "whats the current date" in query:

            date()

        elif "search in google" in query:

            speak("Ok Sir")

            speak("This Is What I Found For Your Search Sir!")
            query = query.replace("search in","")
            query = query.replace("google","")
            kit.search(query)
            sleep(2)
            speak("Done Sir!")

        elif "open history" in query:

            history()

        elif "open downloads" in query:

            downloads()

        elif "open new tab" in query:

            new_tab()
    
        elif "open new window in incognito mode" in query:

            new_window_in_incognito_mode()

        elif "switch tab" in query:

            switch_Tab()

        elif "enable vpn" in query:

            enable_vpn()

        else:
            # If no specific command is recognized, use fallback AI
            # Search memory for relevant context to personalize the response
            memory_ctx = get_memory_context(query)
            response = get_nim_response(query, memory_context=memory_ctx)
            print(f"Fallback AI: {response}")
            speak(response, blocking=False)

if __name__ == "__main__":
    while True:
        permission = take_command()
        if permission == "none":
            continue
        if "wake up" in permission.lower():
            TaskeExecution()