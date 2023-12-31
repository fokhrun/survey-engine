
"""Execute the app"""

from survey_engine import handle_survey, utils


def menu():
    """Main menu"""
    while True:  # Keep running the app
        print()
        print("Survey Engine")
        print("-------------")
        print("1. Create Survey")
        print("2. Participate in Survey")
        print("3. Participate in Survey, Learn results")
        print()

        option = utils.safe_integer_input(valid_range=[1, 2, 3])
        if not option:
            continue

        if option == 1:
            handle_survey.create_survey()
        elif option == 2:
            handle_survey.run_survey(get_statistics=False)
        elif option == 3:
            handle_survey.run_survey()
        else:
            print("\nWrong choice! Try again.\n")

        print()
