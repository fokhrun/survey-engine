""" Handle reponses provided by users """


class Responses:
    """Handles response"""
    FILENAME = "./data/survey_responses.csv"
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
