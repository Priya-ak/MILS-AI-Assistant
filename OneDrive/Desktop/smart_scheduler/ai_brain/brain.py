import ollama

class AIBrain:

    def __init__(self):
        self.model = "phi"

    def think(self, emotion, activity, intent):

        prompt = f"""
        You are MILS, an intelligent productivity assistant.

        Emotion: {emotion}
        Activity: {activity}
        Intent: {intent}

        Suggest what the user should do next in one short sentence.
        """

        try:

            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )

            return response["message"]["content"]

        except Exception:

            return "Continue current activity."