
#### manta - voice assistant ####

import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.8)

def speak(text):
  engine.say(text)
  engine.runAndWait()


def recognize_voice():
  text = ""
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    voice = r.listen(source)
    try:
      text = r.recognize_google(voice)
    except sr.RequestError:
      speak("Sorry, the I can't access the Google API at the moment...")
    except sr.UnknownValueError:
      speak("Sorry, Unable to understand what you're saying...")
  return text.lower()


def reply(text_version):

  if "hello" in text_version:
    speak("Hey there!")

  if "name" in text_version:
    speak("My name is Manta")

  if "how are you" in text_version:
    speak("I am well...")

  if "date" in text_version:
    date = datetime.now().strftime("%-d %B %Y")
    speak(date)

  if "time" in text_version:
    time = datetime.now().time().strftime("%H %M")
    speak("The time is " + time)

  if "search" in text_version:
    speak("What do you want me to search?")
    keyword = recognize_voice()

    if keyword != '':
      url = "https://google.com/search?q=" + keyword
      speak("These are the search results for.." + keyword)
      webbrowser.open(url)
      sleep(3)

  if "quit" in text_version or "exit" in text_version:
    speak("Ok, Exiting. Hope you had a great time!!")
    exit()

sleep(1)

while True:
  text_version = recognize_voice()
  reply(text_version)
