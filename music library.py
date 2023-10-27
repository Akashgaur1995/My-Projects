import pyttsx3
import os
import smtplib
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


    if 'play music' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        music_dir = 'E:\Music'
        songs = os.listdir(music_dir)
    print(songs)    
    os.startfile(os.path.join (music_dir,songs[0]))
