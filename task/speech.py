import speech_recognition as s

#create a object of recognition
sr = s.recognizer()
print("i am your scirpt and listening you...................")
with s.Microphone as m:
    audio = sr.listen(m)
    query = sr.recognize_google(audio,Language= 'eng-in')
    print(query)
    