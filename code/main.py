#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("test.mp3")
    os.system("test.mp3")
   # os.startfile()("test.mp3")
  
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("fine, thnks")

    if "what time is it" in data:
        speak(ctime())
        
    if "hi" in data:
      speak("hi")
        
    if "thank you" in data:
        speak("your welcome")
        
    if "Notepad" in data:
         cmd = 'notepad'
         os.system(cmd)
         
    if "photo" in data:
         cmd = 'start C:\\Users\\BENDIR\\Desktop\\Thomas_Edison2.jpg'
         os.system(cmd)
         
    if "system call" in data:
        cmd = 'start C:\\Users\\BENDIR\\Desktop\\system_call.docx'
        os.system(cmd)
        
    if "Translate" in data:
       webbrowser.open("https://translate.google.com/?hl=fr&sl=fr&tl=ar&op=translate")
       
    if "YouTube" in data:
         webbrowser.open("https://www.youtube.com")
         
    if "Google" in data:
         webbrowser.open("https://google.com")
         
    if "Firefox" in data:
         webbrowser.open("https://www.google.com/search?client=opera&q=mozilla+firefox&sourceid=opera&ie=UTF-8&oe=UTF-8")
    if "close Opera" in data:
        os.system("taskkill /f /im  Opera.exe")
        
      
# initialization
time.sleep(1)
speak("Hello, what can I do for you ?")
while 1:
    data = recordAudio()
    jarvis(data)
