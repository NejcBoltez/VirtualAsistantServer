import pyttsx3 as pyttsx
speech_engine = pyttsx.init()
besedilo="How are you"
speech_engine.say(besedilo)
speech_engine.runAndWait()