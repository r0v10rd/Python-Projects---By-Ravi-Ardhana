from http import client
import speech_recognition as sr 
import pyttsx3 
import webbrowser
import music_lib
import requests
from openai import OpenAI
# recognizer= sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc4024899159804e0e67d"

def speak(text):
    engine.setProperty('rate',115)
    engine.say(text)
    engine.runAndWait()


'''def aiProcess(command):
        client =OpenAI(api_key='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')
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
            {
                "role": "user",
                "content": command
            }])
        return completion.choices[0].message'''


def processcmd(c):
    if "rumble" in c.lower():
        webbrowser.open("https://rumble.com/c/TateSpeech")
    elif  "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif  "gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=music_lib.music[song]  
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=india&apiKey=API_KEY")
        if r.status_code==200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
    
    '''else: #Let Openai handle it.
        output = aiProcess(c)
        print(output)
        speak(output)'''


if __name__== "__main__": # This ensures the code doesn't run when imported
    speak("Pranaam...")
    while True: # This creates an infinite loop
        # obtain audio from the microphone
        r = sr.Recognizer() #instance attribute which converts TtS
        
        # recognize speech using google
        print("recognizing...")
        try:
            with sr.Microphone() as source: # 
                print("Listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=3)
            command = r.recognize_google(audio)
            if "jarvis" in command.lower(): # Listen for the wake word Jarvis
                speak("Ji bhaiya")
                with sr.Microphone() as source:  # with loop opens and closes mic
                    print("Jarvis active...")
                    audio = r.listen(source,timeout=3,phrase_time_limit=3)
                    command= r.recognize_google(audio)
                    speak("Theek hai bhaiya")
                    processcmd(command)
            elif "exit" in command.lower():
                print("Exiting...")
                speak("Exiting")
                break
            print(command)
        
        except Exception as e:
            print("Error; {0}".format(e))