from transformers import pipeline

class QAAgent:

    def __init__(self):

        self.qa = pipeline("question-answering")

    def answer(self, question):

        context = """
        MILS is an intelligent assistant that helps users manage time,
        track productivity, and plan tasks automatically.
        """

        result = self.qa(question=question, context=context)

        return result["answer"]