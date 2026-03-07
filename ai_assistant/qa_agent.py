import ollama


class QAAgent:

    def __init__(self):
        self.model = "phi"


    def build_prompt(self, question, context):

        return f"""
You are MILS, an intelligent AI productivity assistant.

You help the user understand their productivity, schedule, tasks and habits.

--------------------------------
SYSTEM DATA
--------------------------------

Activity: {context.get('activity')}
Emotion: {context.get('emotion')}
Work Type: {context.get('work_type')}

Focus Time: {context.get('focus_time')}
Break Time: {context.get('break_time')}
Distraction Time: {context.get('distraction_time')}

Productivity Score: {context.get('productivity_score')}

Current Task: {context.get('task')}
Next Task: {context.get('next_task')}
Next Task Time: {context.get('next_time')}

AI Decision: {context.get('decision')}

Learned Habits: {context.get('habits')}

--------------------------------
USER QUESTION
--------------------------------

{question}

--------------------------------
INSTRUCTIONS
--------------------------------

Answer clearly like a helpful AI assistant.

If the user asks about productivity:
Explain using Focus Time, Break Time and Productivity Score.

If the user asks about current task:
Tell the Current Task.

If the user asks about schedule:
Explain Current Task and Next Task.

If the user asks for advice:
Use AI Decision and productivity data.

Keep answers short and clear.
"""


    def ask(self, question, context):

        prompt = self.build_prompt(question, context)

        try:

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:

            return "Sorry, I could not generate an answer right now."