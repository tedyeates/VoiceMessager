from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
import speech_recognition as sr
import os
import json
import re


def message_to_speech(message):
    """Uses Google text to speech to get audio of message and play it"""

    # text to speech
    tts = gTTS(text=message)

    # write speech to temp file (playing immediately so no need to store)
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.seek(0)

    # play temp file
    mixer.init()
    mixer.music.load(f)
    mixer.music.play()


def speech_to_message(microphone, recognizer):
    """Uses Google to convert audio to text"""
    with microphone as source:
        # Adjust background noise and get audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = ""
    try:
        response = recognizer.recognize_google(audio, language="en-UK")
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

    return response


def message_emojifier(message):
    """Replace words with corresponding emoji"""
    with open('../resources/EmojiCodeSheet/json/string/all_emojis.json', encoding="utf8") as emojis:
        emoji_dict = json.load(emojis)['Emojis']

        return replace_words(message, emoji_dict)


def replace_words(message, words):
    """Replace keys in a message with other values"""
    for item in words:
        message = message.replace(item['key'], item['value'])

    return message
