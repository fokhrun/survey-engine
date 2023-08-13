# module for suvery setup


class Question:
    """Encode objects"""

    def __init__(self, question_text: str):
        """Initialize variables

        Parameters
        ----------
        question_text : str
            question in text format
        """
        self.question_text = question_text
        self.response_options = None

    def add_response_option(self, options: list[int or str]):
        """add response options to the question

        Parameters
        ----------
        options : list[int or str]
            response options
        """
        self.response_options = options

    def print(self, question_id=1):
        """print question in a terminal"""
        print(f"{question_id}. {self.question_text}")
        if self.response_options:
            for idx, choice in enumerate(self.response_options):
                print(f"{idx + 1}. {choice}")


class Survey:
    def __init__(self, title, num_questions):
        self.survey_title = title
        self.num_questions = num_questions
        self.questions = []  # start with empty questions

    def add_question(self, question: Question):
        if len(self.questions) < self.num_questions:
            self.questions.append(question)

    def print(self):
        print(self.survey_title)
        print (len(self.questions))
        for idx, question in enumerate(self.questions):
            print ("\n")
            question.print(question_id=idx+1)
