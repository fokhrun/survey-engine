""" Handle reponses provided by users """


import csv
import os
from dataclasses import dataclass
from survey_engine import utils


@dataclass
class QuestionOption:
    """Packages question and provided option pair"""
    question: str
    option: int or str


class Responses:
    """Handles response"""
    FIELDNAMES = ["Question", "Response"]
    FILEPATH = "data"

    def __init__(self, survey):
        """
        Initialize response

        Parameters
        ----------
        survey : Survey
            bind response to survey
        """
        self.question_options = []
        self.filename = os.path.join(self.FILEPATH, f"{survey.survey_title}.response")

    def add_question_option(self, question_text, option):
        """
        Add question-option parameter to responses

        Parameters
        ----------
        question : str 
            question text
        option : int 
            chosen option for the question
        """
        self.question_options.append(
            QuestionOption(question=question_text, option=option)
        )

    def save_responses(self):
        """Save response in a csv file"""
        # Here you would save the response to a database or file
        utils.create_file_safely(self.filename, remove_if_exists=False)
        text = ""
        for question_option in self.question_options:
            text += f"{question_option.question},{question_option.option}\n"

        with open(self.filename, "a", encoding="utf") as file:
            file.write(text)
