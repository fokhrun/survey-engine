"""Suvery setup"""


import os
from utils import create_file_safely


class Question:
    """Encode objects"""

    def __init__(self, question_text):
        """
        Initialize variables

        Parameters
        ----------
        question_text : str
            question in text format
        """
        self.question_text = question_text
        self.response_options = None

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
            file.write(f"{self.question_text};{','.join(self.response_options)}\n")

    def print(self, question_id=1):
        """print question in a terminal"""
        print(f"{question_id}. {self.question_text}")
        if self.response_options:
            for idx, choice in enumerate(self.response_options):
                print(f"  {idx + 1}. {choice}")


class Survey:
    """Encode survey object"""

    SURVEY_DIRECTORY = "data/"  # Path where survey question should be saved

    def __init__(self, title, num_questions=1):
        """Initialize variables

        Parameters
        ----------
        title : str
            Survey title
        num_questions : int
            number of questions in the survey, by default 1
        """
        self.survey_title = title
        self.num_questions = num_questions
        self.questions = []  # start with empty questions

    def add_question(self, question):
        """
        Add question to survey

        Parameters
        ----------
        question : Question
            question to add in the survey
        """
        if len(self.questions) < self.num_questions:
            self.questions.append(question)

    def save(self):
        """Save survey to a file"""
        file_path = os.path.join(self.SURVEY_DIRECTORY, f"{self.survey_title}.survey")
        create_file_safely(file_path)
        for question in self.questions:
            question.save_question_to_file(file_path)

    def print(self):
        """Print out survey to terminal"""

        print(self.survey_title)
        for idx, question in enumerate(self.questions):
            print ("\n")
            question.print(question_id=idx+1)
