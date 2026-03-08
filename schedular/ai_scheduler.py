from datetime import datetime
from utils.task_memory import TaskMemory


class AIScheduler:

    def __init__(self):

        self.task_memory = TaskMemory()

        # default daily schedule
        self.schedule = [
            ("Deep Work", "12:00"),
            ("Break", "13:00"),
            ("Study Session", "15:00"),
        ]

    def get_current_time(self):
        return datetime.now().strftime("%H:%M")

    def get_current_task(self):

        now = self.get_current_time()

        current_task = None
        next_task = None
        next_time = None

        # check stored tasks
        tasks = self.task_memory.get_today_tasks()

        for task in tasks:
            if task["time"] <= now:
                current_task = task["task"]
            elif task["time"] > now and next_task is None:
                next_task = task["task"]
                next_time = task["time"]

        # fallback to default schedule
        if not next_task:
            for task, time in self.schedule:
                if time > now:
                    next_task = task
                    next_time = time
                    break

        return {
            "current_task": current_task,
            "next_task": next_task,
            "next_time": next_time
        }