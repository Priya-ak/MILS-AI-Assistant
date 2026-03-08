import json
import datetime
import os


class TaskMemory:

    def __init__(self):

        self.file = "tasks.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def add_task(self, task, time):

        with open(self.file, "r") as f:
            tasks = json.load(f)

        tasks.append({
            "task": task,
            "time": time,
            "date": str(datetime.date.today())
        })

        with open(self.file, "w") as f:
            json.dump(tasks, f, indent=2)

    def get_today_tasks(self):

        today = str(datetime.date.today())

        with open(self.file, "r") as f:
            tasks = json.load(f)

        return [t for t in tasks if t["date"] == today]

    def get_next_task(self):

        tasks = self.get_today_tasks()

        if not tasks:
            return None

        tasks = sorted(tasks, key=lambda x: x["time"])

        return tasks[0]