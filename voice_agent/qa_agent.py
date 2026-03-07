import ollama

class QAAgent:

    def __init__(self):
        self.model = "llama3:latest"

    def ask(self, question, context):

        question = question.lower()

        # Extract context values safely
        task = context.get("task", "No task")
        next_task = context.get("next_task", "None")
        next_time = context.get("next_time", "None")

        focus = context.get("focus_time", 0)
        break_time = context.get("break_time", 0)
        distraction = context.get("distraction_time", 0)
        score = context.get("productivity_score", 0)

        decision = context.get("decision", "No decision yet")
        emotion = context.get("emotion", "Unknown")

        # ---------------------------
        # Direct answers (no AI needed)
        # ---------------------------

        if "productivity" in question:

            return f"""
Your productivity summary:

Current Task: {task}

Focus Time: {focus} minutes
Break Time: {break_time} minutes
Distraction Time: {distraction} minutes

Productivity Score: {score}%

AI Decision: {decision}
"""

        if "next task" in question:

            return f"Your next task is {next_task} at {next_time}."

        if "current task" in question or "my task" in question:

            return f"Your current task is {task}."

        # ---------------------------
        # AI response for general questions
        # ---------------------------

        prompt = f"""
You are MILS AI Assistant.

Current Task: {task}
Next Task: {next_task} at {next_time}

Focus Time: {focus}
Break Time: {break_time}
Distraction Time: {distraction}

Productivity Score: {score}

Emotion: {emotion}
Decision: {decision}

User question:
{question}

Answer clearly and briefly.
"""

        try:

            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )

            return response["message"]["content"]

        except Exception as e:

            print("AI ERROR:", e)

            return "AI assistant could not respond."