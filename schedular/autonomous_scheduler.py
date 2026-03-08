import time


class AutonomousScheduler:

    def __init__(self):

        self.last_activity = None
        self.activity_start_time = time.time()

    def check(self, activity, focus_time, break_time):

        now = time.time()

        # detect activity change
        if activity != self.last_activity:
            self.last_activity = activity
            self.activity_start_time = now

        duration = now - self.activity_start_time

        # Deep work session
        if activity in ["coding", "typing", "studying", "researching"]:

            if duration > 2700:  # 45 minutes
                return "You have been working for 45 minutes. I scheduled a 5 minute break."

        # Long break
        if activity in ["relaxing", "using_phone", "watching_video"]:

            if duration > 600:  # 10 minutes
                return "Break time is over. Let's return to work."

        # Idle detection
        if activity == "idle" and duration > 300:
            return "You have been idle for a while. Start your next task."

        return None