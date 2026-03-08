from utils.task_memory import TaskMemory


class VoiceAssistant:

    def __init__(self):
        self.task_memory = TaskMemory()


    def process_command(self, user_input):

        user_input = user_input.lower()

        # -------------------------
        # Schedule task
        # -------------------------
        if "schedule" in user_input or "remind me" in user_input:

            words = user_input.split()

            time = None

            for w in words:
                if ":" in w or "." in w:
                    time = w.replace(".", ":")

            if not time:
                return "Please tell the time."

            task = user_input.replace("schedule", "").replace("remind me", "").strip()

            self.task_memory.add_task(task, time)

            return f"Task {task} scheduled at {time}"


        # -------------------------
        # Today's tasks
        # -------------------------
        if "today task" in user_input or "my tasks today" in user_input:

            tasks = self.task_memory.get_today_tasks()

            if not tasks:
                return "You have no tasks today."

            msg = "Your tasks today are "

            for t in tasks:
                msg += f"{t['task']} at {t['time']}. "

            return msg


        # -------------------------
        # Next task
        # -------------------------
        if "next task" in user_input:

            task = self.task_memory.get_next_task()

            if not task:
                return "No upcoming tasks."

            return f"Your next task is {task['task']} at {task['time']}"


        # -------------------------
        # Default
        # -------------------------
        return "I did not understand that command."