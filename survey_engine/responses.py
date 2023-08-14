""" Handle reponses provided by users """


import csv
import os
from dataclasses import dataclass
from survey_engine import constants, statistics, utils


@dataclass
class QuestionOption:
    """Packages question and provided option pair"""
    question: str
    option: int or str


class Responses:
    """Handles response"""
    FIELDNAMES = ["Question", "Response"]

    def __init__(self, survey):
        """
        Initialize response

        Parameters
        ----------
        survey : Survey
            bind response to survey
        """
        self.question_options = []
        self.filename = os.path.join(
            constants.SURVEY_DIRECTORY,
            f"{survey.survey_title}{constants.SURVEY_RESPONSE_FILE_EXT}"
        )

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

    def load_responses(self):
        """
        Read saved responses

        Returns
        -------
            Response : Response encoded from csv file
        """
        with open(self.filename, "r", encoding="utf") as csvfile:
            response = list(
                csv.DictReader(csvfile, fieldnames=self.FIELDNAMES)
            )

        responses = {}
        for _ in response:
            question = _[self.FIELDNAMES[0]]
            response = int(_[self.FIELDNAMES[1]])

            if question not in responses:
                responses[question] = [response]
            else:
                responses[question].append(response)

        return responses

    def analyze_responses(self):
        """Analyze responses in quartiles"""

        responses = self.load_responses()

        for question_option in self.question_options:
            values = responses[question_option.question]
            option = question_option.option
            qnt1, median, qnt3 = statistics.calculate_quantiles(values)
            position = statistics.determine_position_in_quantiles(
                response=option,
                quantiles=(qnt1, median, qnt3)
            )

            print("Quantile Analysis:")
            print(f"25th, 50th, 75th Percentile: {qnt1}, {median}, {qnt3}")
            print(f"Current Response: {option} is in Position: {position}")
            print()
