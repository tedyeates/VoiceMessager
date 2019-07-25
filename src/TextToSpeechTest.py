from gtts import gTTS
from playsound import playsound

tts = gTTS(text="Hello Ted, I can pronounce Egle perfectly")
tts.save("greetings.mp3")
playsound("greetings.mp3")
