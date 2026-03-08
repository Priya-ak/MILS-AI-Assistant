import time


class ProductivityTracker:

    def __init__(self):

        self.focus_time = 0
        self.break_time = 0
        self.distraction_time = 0

        self.last_update = time.time()

    def update(self, activity, work_type):

        now = time.time()
        elapsed = now - self.last_update
        self.last_update = now

        # Productive work
        if work_type == "organizational_work":
            self.focus_time += elapsed

        # Personal break
        elif work_type == "personal_activity":
            self.break_time += elapsed

        # Neutral / distraction
        elif work_type == "neutral":
            self.distraction_time += elapsed

    def get_productivity_score(self):

        total = self.focus_time + self.break_time + self.distraction_time

        if total == 0:
            return 0

        score = (self.focus_time / total) * 100
        return round(score, 2)

    def get_stats(self):

        return {
            "focus_time": round(self.focus_time, 1),
            "break_time": round(self.break_time, 1),
            "distraction_time": round(self.distraction_time, 1),
            "productivity_score": self.get_productivity_score()
        }