import pyttsx3
import time

class VoiceAssistant:

    def __init__(self):

        self.engine = pyttsx3.init()
        self.engine.setProperty("rate",150)

        self.last_message = ""
        self.last_time = time.time()

    def speak(self, text):

        if text == self.last_message:
            return

        self.last_message = text

        print("MILS:", text)

        self.engine.say(text)
        self.engine.runAndWait()