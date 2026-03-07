import datetime


class DayPlanner:

    def __init__(self):

        self.schedule = [
            {"time": "09:00", "task": "Start working"},
            {"time": "11:00", "task": "Take a short break"},
            {"time": "13:00", "task": "Lunch break"},
            {"time": "14:00", "task": "Resume work"},
            {"time": "17:00", "task": "Wrap up tasks"}
        ]

    def plan(self, decision):

        now = datetime.datetime.now().strftime("%H:%M")

        for task in self.schedule:

            if now == task["time"]:
                print("Scheduled Task:", task)

        if decision == "Take a short break":
            print("Planner Suggestion: Take a break now")

        if decision == "Start your next task":
            print("Planner Suggestion: Start a productive task")