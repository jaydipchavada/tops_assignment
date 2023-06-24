import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Say something
engine.say("Hello world!")

# Run the engine
engine.runAndWait()
