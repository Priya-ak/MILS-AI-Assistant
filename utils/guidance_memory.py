class GuidanceMemory:

    def __init__(self):
        self.last_message = None
        self.last_time = 0

    def should_speak(self, message, current_time, interval=12):

        if message != self.last_message or current_time - self.last_time > interval:

            self.last_message = message
            self.last_time = current_time
            return True

        return False