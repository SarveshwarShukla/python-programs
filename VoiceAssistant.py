# Program for a configurable voice assistant
# Sarveshwar Shukla (20 March 2022)

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os

def speechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognising...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Recognising unsuccessful")
            return "Recognising Unsuccessful"
            
            
def textToSpeech(textPassed):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    speechRate = engine.getProperty("rate")
    engine.setProperty("rate", 180)
    engine.say(textPassed)
    engine.runAndWait()
            
            
if __name__ == "__main__":
    
    while True:
        dataReceived = speechToText().lower()
        if "my name" in dataReceived:
            toSpeak = "Your name is Sarveshwar" 
            textToSpeech(toSpeak)
        elif "your name" in dataReceived:
            toSpeak = "My name is Jarvis"
            textToSpeech(toSpeak)
        elif "am" in dataReceived:
            toSpeak = "Captain"
            textToSpeech(toSpeak)
        elif "time" in dataReceived:
            toSpeak = datetime.datetime.now().strftime("%I%M%p")
            textToSpeech(toSpeak)
        elif "youtube" in dataReceived:
            webbrowser.open("https://www.youtube.com/")
        elif "music" or "song" in dataReceived:
            musicAddress = "D:/Files/Music"
            listSongs = os.listdir(musicAddress)
            print(listSongs)
            os.startfile(os.path.join(musicAddress, listSongs[0]))
            
        elif "exit" in dataReceived:
            break
            
            

# speechToText()
# textToSpeech("Hello, How are you sarveshwar")