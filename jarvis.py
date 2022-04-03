from http import server
from sys import path
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
from requests import get
from playsound import playsound
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) There are two inbuilt voices in our devices
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jim Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string outputs

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query





# Mail function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shaikhgufrana15@gmail.com', '8291648713')
    server.sendmail('shaikhgufrana15@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:   
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open w3school' in query:
            webbrowser.open("www.w3schools.com")        
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\MEHFUZ\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open pictures' in query:
            picture_dir = 'C:\\Users\\MEHFUZ\\Pictures'
            #pictures = os.listdir(picture_dir)
            #print(pictures)
            #os.startfile(os.path.join(picture_dir))
            os.startfile(picture_dir)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\MEHFUZ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f'your IP address is {ip}')
            speak(f'your IP address is {ip}')
        
        elif 'open whatsapp' in query:
            webbrowser.open("C:\\Users\\MEHFUZ\\AppData\\Local\\WhatsApp\\WhatsApp.exe")  

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "skmehfuz1872@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")
        
        elif 'open map' in query:
            webbrowser.open("https://www.google.com/maps")

       