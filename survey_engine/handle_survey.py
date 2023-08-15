""" Manage surveys """


import os
from survey_engine import constants, responses, surveys, utils


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
    print()
    survey_title = input("Enter survey title: ")
    num_questions = utils.safe_integer_input(
        valid_range=range(1, constants.MAX_QUESTIONS + 1),
        text_prompt="Number of questions: "
    )

    if not num_questions:
        return

    survey = surveys.Survey(survey_title)

    for _ in range(num_questions):
        survey.add_question(create_question())

    survey.print()
    print()
    survey.save()


def load_survey(file_path="data"):
    """
    Load saved surveys

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
    survey_names = [
        _ for _ in os.listdir(file_path)
        if constants.SURVEY_FILE_EXT in _
    ]
    for idx, filename in enumerate(survey_names):
        print(f"{idx + 1}. {utils.get_filename_without_extension(filename)}")

    chosen_survey_idx = utils.safe_integer_input(
        valid_range=range(1, len(survey_names) + 1)
    ) - 1

    survey_filename = survey_names[chosen_survey_idx]
    survey = surveys.Survey(
        utils.get_filename_without_extension(survey_filename)
    )

    name = os.path.join(file_path, survey_filename)
    with open(name, "r", encoding="utf") as file:

        for row in file:
            row = row.strip("\n").split(";")
            survey.add_question(
                surveys.Question(
                    question_text=row[0].strip(),
                    options=[_.strip() for _ in row[1].split(",")]
                )
            )

    return survey


def run_survey(get_statistics=True):
    """
    Run survey

    Parameters
    ----------
    get_statistics : bool
        enable statistics calculation for survey response
        defaults to True
    """
    print()
    survey = load_survey()

    print(f"Welcome to the {survey.survey_title}!")
    print()
    resp_obj = responses.Responses(survey)

    for idx, question in enumerate(survey.questions, start=1):
        question.print(question_id=idx)
        valid_range = range(1, len(question.response_options) + 1)

        option = utils.safe_integer_input(
            valid_range=valid_range,
            text_prompt="Choose survey: "
        )
        if not option:
            return

        resp_obj.add_question_option(
            question_text=question.question_text,
            option=option
        )

        print()

    resp_obj.save_responses()

    if get_statistics:
        resp_obj.analyze_responses()
