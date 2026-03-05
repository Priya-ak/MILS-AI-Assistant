import time

class GuidanceSystem:

    def __init__(self, voice):

        self.voice = voice
        self.last_time = 0
        self.interval = 20
        self.last_decision = ""

    def update(self, decision):

        now = time.time()

        if decision != self.last_decision:

            self.voice.speak(decision)
            self.last_decision = decision

        elif now - self.last_time > self.interval:

            self.voice.speak(f"My suggestion: {decision}")

        self.last_time = now