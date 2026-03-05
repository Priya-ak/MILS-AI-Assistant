class DecisionModel:

    def decide(self, activity, emotion, work_type):

        if emotion == "sad":
            return "Take a break"

        if activity == "phone_usage":
            return "Limit phone use and focus on work"

        if activity == "idle":
            return "Start a productive task"

        if activity == "working":
            return "Continue your work"

        return "Stay productive"