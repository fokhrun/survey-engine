""" Create surveys"""


from survey_engine import survey


def create_question():
    question_text = input("Enter question text: ")
    options = input("Enter response options as comma separated values: \n")
    question = survey.Question(question_text)
    question.add_response_option([_.strip() for _ in options.split(",")])
    question.print()
