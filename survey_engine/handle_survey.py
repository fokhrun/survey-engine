""" Manage surveys """


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
    survey = surveys.Survey(survey_title)
    if num_questions > MAX_QUESTIONS:
        raise ValueError(f"You must chooise {MAX_QUESTIONS} or less")
    for _ in range(num_questions):
        survey.add_question(create_question())
    survey.print()
    survey.save()


def load_survey(file_path="data", survey_extension=".survey"):
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
    survey_names = [
        _ for _ in os.listdir(file_path) 
        if survey_extension in _
    ]

    for idx, filename in enumerate(survey_names):
        print (f"{idx + 1}. {utils.get_filename_without_extension(filename)}")

    survey_filename = survey_names[int(input("Choose survey: "))-1]
    survey = surveys.Survey(utils.get_filename_without_extension(survey_filename))

    with open(os.path.join(file_path, survey_filename), "r", encoding="utf") as file:
        for row in file:
            row = row.strip("\n").split(";")

            survey.add_question(
                surveys.Question(
                    question_text=row[0].strip(),
                    options=[
                        _.strip() for _ in row[1].split(",")
                    ]
                )
            )

    return survey


def safe_input(valid_range, num_retries=3):
    """
    Handles incorrectly provided options

    Parameters
    ----------
    valid_range : list 
        range of values for valid options
    num_retries : int 
        number of times a wrong option can be provided. Defaults to 3.

    Raises:
        ValueError: if wrong option is provided

    Returns:
        int
    """
    error_text_terminate = "You have no more trials left. Terminating...!"

    for attempt_no in range(num_retries):
        option = int(input("Enter your choice: "))

        if option not in valid_range:
            option = None
            remaining_trials = num_retries-attempt_no-1

            if remaining_trials == 0:
                raise ValueError(error_text_terminate)

            error_text = f"You have {remaining_trials} more trials!"
            print (f"Not a valid option. Please try again! {error_text}")
        else:
            return option


def run_survey(get_statistics=True):
    """
    Run survey
    
    Parameters
    ----------
    get_statistics : bool
        enable statistics calculation for survey response
        defaults to True
    """
    survey = load_survey()

    print(f"Welcome to the {survey.survey_title}!")
    resp_obj = responses.Responses(survey)

    for idx, question in enumerate(survey.questions, start=1):
        question.print(question_id=idx)
        valid_range = range(1, len(question.response_options)+1)
        option = safe_input(valid_range)
        resp_obj.add_question_option(question_text=question.question_text, option=option)
    resp_obj.save_responses()
    if get_statistics:
        resp_obj.analyze_responses()
