import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import songs
import requests
from openai import OpenAI
# from gtts import gTTS
# import os
# from gtts import gTTS
# import pygame





recognizer=sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
        
    client = OpenAI(api_key="")

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4", "gpt-3.5-turbo", etc.
        messages=[
            {"role": "system", "content": "You are a vietual assistant named jarvis skilled in general tasks like alexa and google.answer in 1 line"},
            {"role": "user", "content": command}
        ]
    )
    print(response.choices[0].message.content)
    speak(response.choices[0].message.content)
    



def processcommand(c):
  
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening you tube")
        webbrowser.open("https://youtube.com")
    elif "open twitter" in c.lower():
        speak("opening twitter")
        webbrowser.open("https://twitter.com")
    elif "news" in c.lower():
        api_key = "your api key"  # replace with your new key
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        try:
            print(f"Fetching news from: {url}")
            r = requests.get(url, timeout=5)
            print(f"Status code: {r.status_code}")
            print(f"Response: {r.text}")  # See the raw JSON

            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    speak(f"Here are the top {min(5, len(articles))} news headlines.")
                    time.sleep(2)
                    for article in articles[:5]:
                        title = article.get('title', 'No title available')
                        print(f"Speaking: {title}")
                        engine.say(title)
                        
                else:
                    speak("No news found.")
            else:
                speak(f"Failed to fetch news. Error code {r.status_code}")
        except Exception as e:
            speak("There was a problem fetching the news.")
            print(f"News error: {e}")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=songs.music[song]
        webbrowser.open(link)
    else:
        output=aiprocess(c)
        print(command)

        




if __name__=="__main__":
    
    speak("intializing jarvis........")
    
    
    while True:
        r=sr.Recognizer()
        print("recognizing......")
        
        try:
            with sr.Microphone() as source:
                print("listening.....")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                engine.say("ya,how can i help you?")
                
                
                
            # listen the command
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    print(command)
                    processcommand(command)
                    
        except Exception as e:
            print("error; {0}".format(e))

