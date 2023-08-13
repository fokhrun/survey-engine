""" Create surveys """


from survey_engine import surveys


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
