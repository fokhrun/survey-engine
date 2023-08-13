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
        self.response_options = []

    def add_response_option(self, options: list[any]):
        """add response options to the question

        Parameters
        ----------
        options : list[any]
            response options
        """
        self.response_options = options

    def print_question(self):
        """print question in a terminal"""
        print(self.question_text)
        if not self.response_options:
            for idx, choice in enumerate(self.response_options, start=1):
                print(f"{idx}. {choice}")
