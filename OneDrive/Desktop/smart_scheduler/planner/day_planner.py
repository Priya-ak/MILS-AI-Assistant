import datetime

class DayPlanner:

    def plan(self, decision):

        now = datetime.datetime.now()

        task = {
            "time": now.strftime("%H:%M"),
            "task": decision
        }

        print("Scheduled Task:", task)