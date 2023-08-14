"""Suvery setup"""


import os
from survey_engine import utils, constants


class Question:
    """Encode objects"""

    def __init__(self, question_text, options=None):
        """
        Initialize variables

        Parameters
        ----------
        question_text : str
            question in text format
        options : list
            response options, default to None
        """
        self.question_text = question_text
        self.response_options = [] if not options else options

    def add_response_option(self, options):
        """
        Add response options to the question

        Parameters
        ----------
        options : list[int or str]
            response options
        """
        self.response_options = options

    def save_question_to_file(self, file_path):
        """
        Save question to a selected file

        Parameters
        ----------
        file_path : str
            path where the survey question should be saved
        """
        with open(file_path, "a", encoding="utf8") as file:
            file.write(
                f"{self.question_text};{','.join(self.response_options)}\n"
            )

    def print(self, question_id=1):
        """print question in a terminal"""
        print(f"{question_id}. {self.question_text}")
        if self.response_options:
            for idx, choice in enumerate(self.response_options):
                print(f"  {idx + 1}. {choice}")


class Survey:
    """Encode survey object"""

    def __init__(self, title):
        """Initialize variables

        Parameters
        ----------
        title : str
            Survey title
        """
        self.survey_title = title
        self.questions = []  # start with empty questions

    def add_question(self, question):
        """
        Add question to survey

        Parameters
        ----------
        question : Question
            question to add in the survey
        """
        self.questions.append(question)

    def save(self):
        """Save survey to a file"""

        filename = utils.convert_filename(self.survey_title)
        file_path = os.path.join(
            constants.SURVEY_DIRECTORY,
            f"{filename}_{len(self.questions)}{constants.SURVEY_FILE_EXT}"
        )
        utils.create_file_safely(file_path)

        for question in self.questions:
            question.save_question_to_file(file_path)

    def print(self):
        """Print out survey to terminal"""

        print(self.survey_title)
        print()
        for idx, question in enumerate(self.questions):
            print("\n")
            question.print(question_id=idx+1)
            print()
