class ContextMemory:

    def __init__(self):
        self.previous_activity = None
        self.previous_intent = None
        self.previous_emotion = None

    def update(self, activity, intent, emotion):

        self.previous_activity = activity
        self.previous_intent = intent
        self.previous_emotion = emotion

    def get_context(self):

        return {
            "activity": self.previous_activity,
            "intent": self.previous_intent,
            "emotion": self.previous_emotion
        }