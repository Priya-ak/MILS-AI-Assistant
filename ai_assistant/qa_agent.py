import ollama


class QAAgent:

    def __init__(self):
        self.model = "phi3"   # correct model


    def build_prompt(self, question, context):

        return f"""
You are MILS, an intelligent productivity assistant.

SYSTEM DATA

Activity: {context.get('activity')}
Emotion: {context.get('emotion')}
Work Type: {context.get('work_type')}

Focus Time: {context.get('focus_time')}
Break Time: {context.get('break_time')}
Distraction Time: {context.get('distraction_time')}

Productivity Score: {context.get('productivity_score')}

Current Task: {context.get('current_task')}
Next Task: {context.get('next_task')}
Next Task Time: {context.get('next_time')}

AI Decision: {context.get('decision')}

USER QUESTION:
{question}

Instructions:

1. If user asks about productivity:
Explain focus time, break time and productivity score.

2. If user asks about current task:
Tell the current task.

3. If user asks about next task:
Tell the next task and time.

4. If user asks what to do next:
Give advice using AI decision.

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
            return f"AI error: {str(e)}"