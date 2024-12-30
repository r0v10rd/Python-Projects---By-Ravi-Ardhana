import pygame
import pyttsx3 as p3
from gtts import gTTS
import speech_recognition as sr
# r = sr.Recognizer()
engine= p3.init()
voices= engine.getProperty('voices')
def speak(text):
    engine.setProperty('rate',115)
    # engine.setProperty('volume',1)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

'''def speak(text):
    tts = speak(text)
    tts.save("temp.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the MP3 file
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        continue'''


if __name__=="__main__":
    while True:
        text =input("Type text to speak:")
        if text.lower()=="exit tts":
            speak("Exiting")
            break
        else:
            speak(text)

# # TO GET INFO ABOUT VOICES
# for index,voice in enumerate(voices):
#     print(f"Voice {index}:")
#     print(f"  - ID: {voice.id}")
#     print(f"  - Name: {voice.name}")
#     print(f"  - Gender: {voice.gender}")
#     print(f"  - Languages: {voice.languages}")