import speech_recognition as sr

for index,name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print(r.recognize_google(audio))
