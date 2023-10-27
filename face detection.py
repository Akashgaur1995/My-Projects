import pyttsx3
import speech_recognition as sr
import datetime
import os
import smtplib
import face_detection
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

    speak("I am Logan Sir. Please tell me how may I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    # r = face_detection.Recognizer()
    # with face_detection.camera() as source:
    #     print("capturing")
    #     r.pause_threshold = 1
    #     # audio = r.listen(source)
    query = takeCommand().lower()
    if 'open camera' in query:
            face_detection.open("camera")