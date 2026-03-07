import datetime


class AIScheduler:

    def __init__(self):

        self.schedule = {
            "09:00": "Morning Planning",
            "10:00": "Deep Work Session",
            "11:30": "Short Break",
            "12:00": "Research Work",
            "13:00": "Lunch Break",
            "14:00": "Project Development",
            "16:00": "Learning / Study",
            "18:00": "Daily Review"
        }

    def get_current_task(self):

        now = datetime.datetime.now().strftime("%H:%M")

        times = sorted(self.schedule.keys())

        current_task = None
        next_task = None
        next_time = None

        for i, time in enumerate(times):

            if now >= time:
                current_task = self.schedule[time]

                if i + 1 < len(times):
                    next_time = times[i + 1]
                    next_task = self.schedule[next_time]

        # If no next task → start tomorrow schedule
        if next_task is None:
            next_time = times[0]
            next_task = self.schedule[next_time]

        return {
            "current_task": current_task,
            "next_task": next_task,
            "next_time": next_time
        }