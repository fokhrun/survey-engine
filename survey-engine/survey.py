# module for suvery setup


class Question:
    def __init__(self, question_text: str):

        self.question_text = question_text
        self.response_options = []
