class ProductivityTracker:

    def __init__(self):
        self.score = 50

    def update(self, activity, intent):

        if intent in ["work", "study"]:
            if activity != "Using Phone":
                self.score += 2
            else:
                self.score -= 1

        if intent == "sleep":
            self.score -= 2

        if intent == "fitness":
            self.score += 1

        self.score = max(0, min(100, self.score))

        return self.score