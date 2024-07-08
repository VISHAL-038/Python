import cowsay
import pyttsx3
voice = pyttsx3.init()
data  =input("What's this?")
if len(data)< 10:
    cowsay.cow(data)
    voice.say(data)
    voice.runAndWait()
else:
    cowsay.trex(data)
    voice.say(data)
    voice.runAndWait()