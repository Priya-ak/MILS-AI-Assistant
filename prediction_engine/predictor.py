class ActivityPredictor:

    def predict(self, activity, emotion, intent):

        if intent == "sleep":
            return "Sleeping soon"

        if intent == "fitness":
            return "Going to gym"

        if emotion == "tired":
            return "Resting soon"

        if activity == "Using Phone":
            return "Checking messages"

        return "Continuing activity"