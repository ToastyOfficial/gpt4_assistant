# Made by Toasty | 614 eShop x Dawnstar

from os import system
import speech_recognition as sr
from playsound import playsound
from gpt4all import GPT4All
import sys
import whisper
import warnings
import time
import os

wake_word = 'friday'
model = GPT4All("/Users/Toasty/AppData/Local/nomic.ai/GPT4All/ggml-model-gpt4all-falcon-q4_0.bin")# this is mine. Won't work
# Windows /Users/YourUser/AppData/Local/nomic.ai/GPT4All
# MacOS "Users/Toasty/Library/Application Support/nomic.ai/GPT4All"
r = sr.Recognizer()
tiny_model = whisper.load_model('tiny')
base_model = whisper.load_model('base')
listening_for_wake_word = True
source = sr.Microphone()

if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init() 

def speak(text): # if MacOS
    if sys.platform == 'darwin': 
        ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    else:
        engine.say(text) # if Windows/Linux
        engine.runAndWait()

def listen_for_wake_word(audio): # <-- records your audio prompt and saves it.
    global listening_for_wake_word
    with open("wake_detect.wav", "wb") as f:
        f.write(audio.get_wav_data())
    result = tiny_model.transcribe('wake_detect.wav')
    text_input = result['text']
    if wake_word in text_input.lower().strip():
        print("Hello Sir, Please tell me how I may assist you today.")
        speak('Listening')
        listening_for_wake_word = False

def prompt_gpt(audio): # <-- records your audio prompt and saves it.
    global listening_for_wake_word
    try:
        with open("prompt.wav", "wb") as f:
            f.write(audio.get_wav_data())
        result = base_model.transcribe('prompt.wav')
        prompt_text = result['text']
        if len(prompt_text.strip()) == 0:
            print("Empty prompt. Please speak again.")
            speak("Empty prompt. Please speak again.")
            listening_for_wake_word = True
        else:
            print('User: ' + prompt_text)
            output = model.generate(prompt_text, max_tokens=200)
            print('F.R.I.D.A.Y.: ', output)
            speak(output)
            print('\nSay', wake_word, 'to get started. \n')
            listening_for_wake_word = True
    except Exception as e:
        print("Prompt error: ", e)

def callback(recognizer, audio):
    global listening_for_wake_word
    if listening_for_wake_word:
        listen_for_wake_word(audio)
    else:
        prompt_gpt(audio)

def start_listening():
    with source as s:
        r.adjust_for_ambient_noise(s, duration=2)
        print('\nSay', wake_word, 'to get started. \n')
        
        global listening_for_wake_word
        while True: 
            audio = r.listen(s) # <-- working on other method
            if listening_for_wake_word:
                listen_for_wake_word(audio)
            else:
                prompt_gpt(audio)
            time.sleep(1)

if __name__ == '__main__':
    start_listening() 