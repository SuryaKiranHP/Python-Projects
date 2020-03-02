import speech_recognition as sr
r = sr.Recognizer()

hello=sr.AudioFile('C:/Users/736398/Desktop/ConvertedAudio/Converted.wav')
with hello as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
