import speech_recognition as sr
import webbrowser
import os
sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=5000
with sr.Microphone() as source:
    print("Diga seu comando, lembra que ainda trabalho em ingles")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print ("Você disse : {}".format(text).lower())
        os.system(text.lower())
    except:
        print("Não entendi")
