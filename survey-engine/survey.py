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

    def add_response_option(self, option: list[any]):
        """add response options to the question

        Parameters
        ----------
        options : list[any]
            response options
        """
        self.response_options.append(option)
