class HabitMemory:

    def __init__(self):
        self.history = []

    def add(self, activity, intent):
        self.history.append((activity, intent))

        if len(self.history) > 20:
            self.history.pop(0)

    def predict_next(self):

        if len(self.history) < 3:
            return "Unknown"

        last = self.history[-1]

        for a, i in reversed(self.history[:-1]):
            if a == last[0] and i == last[1]:
                return i

        return "general"