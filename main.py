import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame

def text_to_speech():

# Using google text-to-speech API
    language = "en"
    text = "My name is Omar Esam and i am a software engineer"
    speech = gTTS(text=text, lang=language, slow=False, tld="com.au")

    # Saving the speech into an mp3 file
    speech.save("speech.mp3")

    # Initializing pygame mixer (For audio playback)
    pygame.mixer.init()

    # Loading the saved audio into the mixer to play
    pygame.mixer.music.load("speech.mp3")

    # Playing the audio
    pygame.mixer.music.play()

    # Ensuring the program won't terminate untill the audio stops playing
    while pygame.mixer.music.get_busy():
        continue

#--------------------------------------------------------------#

def convert_speech_to_text():
    # Initializing recognizer
    r = sr.Recognizer()

    # Using default mic as a source to capture audio from the microphone
    # With keyword handles opening and closing the microphone
    with sr.Microphone() as source:
        print("Please Say something...")
        audio = r.listen(source)
        r.phrase_time_limit = 5 #max duration for recording the audio is 5 sec


    try:
        # Converting process
        # Using google web speech api for speech recognition
        print("Please wait, Recognizing the audio right now..")
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text

        # API Cant recognize the speech
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        # Problem in the request to the API, {0} is a placeholder for the error msg we get from the exception
        # Example on the error: connection timed out
    except sr.RequestError as e:
        print("Error occurred during speech recognition: {0}".format(e))

# After Converting Speech To Text
# Use Google Translate API
# Taking recognized(returned) text and the language to be translated to, then translates it

def translate_text(text, target_language):
    translator = Translator()

    try:
        # Translating Process
        translation = translator.translate(text, dest=target_language)
        print("Translation: " + translation.text)
    except Exception as e:
        print("Error occurred during translation: {0}".format(e))

def speech_to_text():
    text = convert_speech_to_text()
    if text is not None:
        target_language = "es"  #Spanish Lang
        translate_text(text, target_language)

# Calling Functions
speech_to_text()
text_to_speech()
