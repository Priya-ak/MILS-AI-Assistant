import time
from collections import defaultdict


class HabitMemory:

    def __init__(self):

        self.activity_log = []
        self.patterns = defaultdict(list)

    def record_activity(self, activity):

        current_time = time.time()

        self.activity_log.append({
            "activity": activity,
            "time": current_time
        })

    def analyze_patterns(self):

        for i in range(1, len(self.activity_log)):

            prev = self.activity_log[i - 1]
            curr = self.activity_log[i]

            if prev["activity"] == curr["activity"]:

                interval = curr["time"] - prev["time"]

                self.patterns[curr["activity"]].append(interval)

    def get_habits(self):

        habits = {}

        for activity, intervals in self.patterns.items():

            if len(intervals) > 3:

                avg = sum(intervals) / len(intervals)

                habits[activity] = round(avg, 1)

        return habits