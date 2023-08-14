
from survey_engine import handle_survey

def menu():
    while True:
        print ("Survey Engine")
        print ("-------------")
        print ("1. Create Survey")
        print ("2. Participate in Survey")
        print ("3. Participate in Survey, Learn results")

        option = int(input("Enter your choice: "))

        if option == 1:
            handle_survey.create_survey()
        elif option == 2:
            handle_survey.run_survey(get_statistics=False)
        elif option == 3:
            handle_survey.run_survey()
        else:
            print ("\nWrong choice! Try again.\n")
