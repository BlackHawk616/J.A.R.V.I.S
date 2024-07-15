import requests
import os
from PIL import Image
import pyttsx3
from datetime import datetime
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.trace as crrs

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
Api_Key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"

def Space_Info(Date):

    speak("Sir Extracting News From Nasa's Public Data Base")

    Url = "https://api.nasa.gov/planetary/apod?api_key=KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "F:\\jarvis\\" + str(FileName)

    Path_2 = "F:\\jarvis\\database\\Space Images\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    print(f"Title : {Title}")
    print(f"According To Nasa : {Info}")

    speak(f"Title : {Title}")
    speak(f"According To Nasa : {Info}")

def IssTracker():

    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    print(f"Time And Date : {dt}")
    print(f"Latitude : {lat}")
    print(f"Longitude : {lon}")

    speak("Sir, The Internatioanal space station codinaters are")
    speak(f"Latitude : {lat}")
    speak(f"Longitude : {lon}")
    speak("Sir, these are the codinates and also you will able to see in map")

    plt.figure(figsize=(10,8))

    ax = plt.axes(projection = ccrs.PlateCarree())

    ax.stock_img()

    plt.scatter(float(lon),float(lat),color = 'blue' , marker= 'o')

    plt.show()

