class DayPlanner:

    def decide(self, emotion, activity, work):

        if emotion == "sad":
            return "You seem sad. Take a short break."

        if emotion == "fear":
            return "Try to relax and focus on breathing."

        if work == "organizational":
            return "Good time to focus on your work."

        if work == "personal":
            return "You can enjoy some personal time."

        return "Continue current activity."