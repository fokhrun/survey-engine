""" Run existing surveys """


import csv
import os
from survey_engine import surveys, utils


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
    
        survey_idx = int(input("Choose survey: "))
    survey_filename = survey_names[survey_idx]
    survey = surveys.Survey(utils.get_filename_without_extension(survey_filename))

    with open(os.path.join(file_path, survey_filename), "r", encoding="utf") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            survey.add_question(
                surveys.Question(
                    question_text=row[0].strip(),
                    options=[
                        _.strip() for _ in row[1].split(",")
                    ]
                )
            )

    return survey

    
"""
# Present the survey and collect responses
def run_survey_app():
    survey = load_survey()
    print(f"Welcome to the {survey.title}!")
    print("Please answer the following questions:\n")
    responses = Responses(title=survey.title)

    for idx, question in enumerate(survey.questions, start=1):
        question_text = question.question_text
        print(f"{idx}. {question_text}")
        option_range = enumerate(question.response_options, start=1)
        for option_idx, option in option_range:
            print(f"   {option_idx}. {option}")

        valid_range = range(1, len(question.response_options)+1)
        option = safe_input(valid_range)

        if not option:
            msg = "You failed to provide a valid answer. Terminating ...!"
            raise ValueError(msg)
        responses.add_question_option(question=question_text, option=option)

    responses.save_responses()

    print("\n")
    """