import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecaputre as ec
import wolframalpha
import json
import requests
import pyaudio

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("volume", .50)
engine.setProperty('voice', voices[0].id)


def speak(text):
    '''Text to speech with timeout.'''
    engine.say(text)
    engine.runAndWait()

def wishMe():
    '''AI Introduction and time relavent greeting.'''
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    '''Allows the AI to accept and understand human language.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant AI-Ben")
speak("Loading you AI personal assistant AI-Ben")
wishMe()

if __name__=="__main__":

    while True:

        speak("Tell me how can I help you now")
        statement = takeCommand().lower()
        if statement == 0:
            continue
    
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal assistant is shutting down, Good Bye")
            print("Your personal assistant is shutting down, Good Bye")
            break

        if "wikipedia" in statement:
            speak("Searching Wikipedia...")
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is now open")
            time.sleep(5)

        elif "open gmail" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google mail is now open")
            time.sleep(5)

        elif "time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "tell me the news" in statement:
            news = webbrowser.open_new_tab("https://www.reuters.com/")
            speak("Here are some headlines from Reuters, Happy Reading")
            time.sleep(6)

        elif "search" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        
        elif "ask" in statement:
            speak("What question do you have")
            question = takeCommand()
            app_id = "Paste your unique ID here "
            client = wolframalpha.Client("*********")
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "good night" in statement or "shut down" in statement or "shut down computer" in statement:
            speak("Ok, your pc will shut down in 10 sec make sure you exit all applications, good night")
            subprocess.call(["shutdown", "/s"])

        elif "restart" in statement:
            speak("Ok, your pc will shut down in 10 sec make sure you exit all applications, good night")
            subprocess.call(["shutdown", "/r"])

        elif "save to file" in statement:
            save_to_file(statement)