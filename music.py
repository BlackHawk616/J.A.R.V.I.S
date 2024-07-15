from time import sleep
from tokenize import Special
import webbrowser
import pyttsx3
import speech_recognition as sr
from pyautogui import doubleClick
from pyautogui import click


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():

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

def me_my_self():

    webbrowser.open("https://www.youtube.com/watch?v=Ly2sHGl3RkM")

    speak("Sir, Playing G-Eazy x Bebe Rexha - Me, Myself & I (Lyrics Video)")

def heat_waves():

    webbrowser.open("https://youtu.be/rfTgO9rpqck")

    speak("Sir, Playing Glass Animals - Heat Waves")

def infinity():

    webbrowser.open("https://www.youtube.com/watch?v=mpIzEfQjKe4")

    speak("Sir,Playing Infinity Jaymes Young [Lyrics]")

def stereo_hearts():

    webbrowser.open("https://www.youtube.com/watch?v=sLzp9t8Fb7o")

    speak("Sir Playing Gym Class Heroes - Stereo Hearts (feat. Adam Levine)")

def night_changes():

    webbrowser.open("https://www.youtube.com/watch?v=7KPyunRIjr0")

    speak("Sir Playing One Direction - Night Changes (Lyrics)")

def unstoppable():

    webbrowser.open("https://www.youtube.com/watch?v=apUV1DyAv1s")

    speak("Sir, PLaying Sia - Unstoppable (Lyrics)")

def love():

    webbrowser.open("https://www.youtube.com/watch?v=kXtYGMor8dc")

    speak("Sir, Playing Ckay Love Nwantiti - Ckay Love Nwantiti Lyrics")

def Old_Town_Road():

    webbrowser.open("https://www.youtube.com/watch?v=r7qovpFAGrQ")

    speak("Sir Playing Lil Nas X - Old Town Road (Official Video)")

def begging():

    webbrowser.open("https://www.youtube.com/watch?v=7SMw6S_LD9s")

    speak("Sir Playing Måneskin - Beggin (Lyrics)")

def Let_Me_Down():
    
    webbrowser.open("https://www.youtube.com/watch?v=jLNrvmXboj8f")

    speak("Sir PLaying Alec Benjamin - Let Me Down Slowly (Lyrics)")

def In_The_Middle_OF_The_Night():

    webbrowser.open("https://youtu.be/CfgcbCe9Z_o")

    speak("Sir Playing  Middle of the Night (Lyrics)")

def A_Man_Without_Love():

    webbrowser.open("https://www.youtube.com/watch?v=xkpavsRGFC4")

    speak("Sir Playing A Man Without Love ")

def startboy_weekend_draft():

    webbrowser.open("https://www.youtube.com/watch?v=xizN47Box_Y")

    speak("Sir Playing Starboy Weekend Draft")

def ture_love():

    webbrowser.open("https://www.youtube.com/watch?v=FhD-PJvKfJQ")

    speak("Sir Play XXX Tentacion True Love")

def Copy():

    webbrowser.open("https://www.youtube.com/watch?v=pnf7nhYEGqg")

    speak("Sir Playing Copy Kakashi Rap")

def hoes_no_jujustu():

    webbrowser.open("https://www.youtube.com/watch?v=BkizwI_R9_4")

    speak("Sir, Playing Hoes No Jujustu")

def Bad_liar():

    webbrowser.open("https://www.youtube.com/watch?v=uEDhGX-UTeI")
    
    speak("Sir Playing Imagine dragon Bad Liar")

def arcade():

    webbrowser.open("https://www.youtube.com/watch?v=PNozaFzqOvI")

    speak("Sir Playing Arcade")

def idfc():

    webbrowser.open("https://www.youtube.com/watch?v=v0pjeUTad2I")

    speak("Sir Playing IDFC")

def Shape_OF_You():

    webbrowser.open("https://www.youtube.com/watch?v=ENNDD7FMkmA")

    speak("Sir Playing Shape OF You")

def industry():

    webbrowser.open("")

    speak("Sir Playing Industry Baby")

def blinding_lights():

    webbrowser.open("https://www.youtube.com/watch?v=XwxLwG2_Sxk")

    speak("Sir Playing Blinding Lights")

def One_Dance():

    webbrowser.open("https://www.youtube.com/watch?v=ki0Ocze98U8")

    speak("Sir Playing One Dance")

def Billie_eiliesh():

    webbrowser.open("https://www.youtube.com/watch?v=xzdZZ6CXBmI")

    speak("Sir, Playing Billie Eiliesh")

def One_Kiss():

    webbrowser.open("https://www.youtube.com/watch?v=y4bNDvwQobY")

    speak("Sir, Playing One Kiss")

def Play_My_Playlist():
    # Customise This Module According To Your Spotify Playlist
    # you can even add more playlist in this

    speak("Sir, Which Playlist Shall I Play")

    speak("Sir, These Are The Options")

    speak("First Liked playlist")

    speak("second Best playlist")

    speak("third sad song playlist")

    speak("fourth study lofi playlist")

    # speak("fourth Lofi Beats To Study,relax or sleep")

    query = take_command().lower()

    if " play first playlist" in query:

        speak("Ok Sir Playing Liked Playlist")

        doubleClick(x=494, y=766)

        sleep(2)

        doubleClick(x=112, y=249)

        sleep(2)

        speak("Sir Playing Liked playlist")

    elif " play second playlist" in query:

        speak("Ok, Sir Playing Best Playlist playlist")

        doubleClick(x=494, y=766)

        sleep(2)

        doubleClick(x=76, y=479)

        sleep(2)

        speak("Sir Playing Triple X Tentacion Playlist")
        
    elif " play thrid playlist" in query:

        speak("Ok, Sir Playing Sad Songs Playlist")

        doubleClick(x=494, y=766)

        sleep(2)

        doubleClick(x=114, y=344)

        sleep(2)

        speak("Sir playing Sad Songs Playlist")

    elif " play fourth playlist" in query:

        speak("Ok Sir, Playing Study Lofi")

        doubleClick()

        sleep(2)

        doubleClick()

        sleep(2)

        speak("Sir playing Study Lofi")

    else:
        speak("Sorry Sir Unable To Find That Playlist")        

def select_which_device():

    speak("OK Sir, I Which Device Shall I Play")

    doubleClick(x=494, y=766)

    sleep(2)

    click(x=1214, y=723)

    sleep(2)

    speak("Sir Which Device Shall I Connect")

    query = take_command().lower()

    if " connect to tv" in query:

        speak("Ok Sir Connecting and playing In Tv")

        click(x=1159, y=603)

        speak("Sir Playing On TV")

    elif " play on my device" in query:

        speak("Ok Sir playing On This")

        click(x=1159, y=603)

        speak("OK Sir Playing on this device")


    elif " on mobile" in query:

        speak("Ok Sir, Connecting TO Mobile")

        click()

        speak("Sir Playing On Mobile")

    else:
        speak("Unable To Find The Device Sir")
