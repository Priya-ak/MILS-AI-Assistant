class BehaviorEngine:

    def decide(self, activity, emotion):

        if emotion == "sad":
            return "Take a short break"

        if activity == "phone_usage":
            return "Limit phone use and focus on work"

        if activity == "idle":
            return "Start a productive task"

        if activity == "working":
            return "Continue your work"

        return "Stay productive"