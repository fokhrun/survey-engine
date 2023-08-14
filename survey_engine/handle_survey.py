""" Create surveys """


import csv
import os
from survey_engine import surveys, responses, utils


MAX_QUESTIONS = 5


def create_question():
    """Create question for the surveys"""

    question_text = input("Enter question text: ")
    options = input("Enter response options as comma separated values: \n")

    question = surveys.Question(question_text)
    response_options = [_.strip() for _ in options.split(",")]
    question.add_response_option(response_options)

    return question


def create_survey():
    """
    Create survey

    Raises
    ------
    ValueError
        if number of questions chosen by a user is larger 
        than a recommended limit
    """
    survey_title = input("Enter survey title: ")
    num_questions = int(input("Enter number of questions: "))
    survey = surveys.Survey(title=survey_title, num_questions=num_questions)
    if num_questions > MAX_QUESTIONS:
        raise ValueError(f"You must chooise {MAX_QUESTIONS} or less")
    for _ in range(num_questions):
        survey.add_question(create_question())
    survey.print()
    survey.save()


def load_survey(file_path="data", file_extension=".survey"):
    """_summary_

    Parameters
    ----------
    file_path : str
        path to find survey files
    file_extension : str
        file extension of the surveys, defaults t0 .survey
    
    Returns
    -------
        Survey
    """
    survey_names = os.listdir(file_path)
    for idx, filename in enumerate(survey_names):
        print (f"{idx + 1}. {utils.get_filename_without_extension(filename)}")

    survey_filename = survey_names[int(input("Choose survey: "))-1]
    survey = surveys.Survey(utils.get_filename_without_extension(survey_filename))
    
    with open(os.path.join(file_path, survey_filename), "r", encoding="utf") as file:
        for row in file:
            row = row.strip("\n").split(";")
            print (row)
            survey.add_question(
                surveys.Question(
                    question_text=row[0].strip(),
                    options=[
                        _.strip() for _ in row[1].split(",")
                    ]
                )
            )

    return survey


def run_survey():
    survey = load_survey()
    print(f"Welcome to the {survey.survey_title}!")
    resp_obj = responses.Responses(survey)
    survey.print()

