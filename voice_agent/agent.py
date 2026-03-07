import ollama


class VoiceAgent:

    def __init__(self):
        self.model = "llama3"

    def respond(self, question):

        prompt = f"""
        You are MILS, a friendly AI productivity assistant.
        Answer the user's question.

        Question:
        {question}
        """

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]