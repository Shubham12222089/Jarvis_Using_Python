import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit


engine = pyttsx3.init('sapi5') #it will provide the engine which will be used in the speak function

voices = engine.getProperty('voices')

# print(voices[0].id)  ---> david voice
# print(voices[0].id)  ---> zira voice

engine.setProperty('voices',voices[0].id)

#function to convert text to audio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#take function is used to take input from the user
#convert Voice to text
def takeCommand():
    r = sr.Recognizer() # defined recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 #if we take a pause in between speaking , then our jarvis should not 
        # leave the recognization

        audio = r.listen(source,timeout=1,phrase_time_limit=5)

#exception handling
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        speak("Say that again Please...")
        return None
    return query


#wish function:

def wish():
    hour = int(datetime.datetime.now().hour)

    if(hour>0 and hour<=12):
        speak("Good Morning")
    elif(hour>12 and hour<18):
        speak("Good AfterNoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir, Please tell me how can i help you...")

if __name__ == "__main__": #iske andar jo bhi program likhenge wo isi ke andar run honge.
    #speak("Hi shubham, This is advance Jarvis")
    #takeCommand()
    wish()

    #while True:
    if True: #runs only one time

        query = takeCommand().lower()

        #logic building for task

        if "open notepad" in query:
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2401.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            #now we have to import os module
            os.startfile(npath)
        elif "open google chrome" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "C:\\Users\\shubh\\Music"
            songs = os.listdir(music_dir)
            s = random.choice(songs)
            os.startfile(os.path.join(music_dir,s))

        elif "wikipedia" in query:
            speak("Opeaning wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            #print(results)
        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif "open github" in query:
            speak("Opeaning github sir")
            webbrowser.open("www.github.com")
        elif "open youtube" in query:
            speak("Opeaning youtube sir")
            webbrowser.open("www.youtube.com")
        elif "play song on youtube" in query:
            speak("which song should i play sir")
            so = takeCommand().lower()
            pywhatkit.playonyt(f"{so}")
