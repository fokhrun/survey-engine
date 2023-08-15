
"""Utility functions"""

import os
from survey_engine import utils


def create_file_safely(file_path, remove_if_exists=True):
    """
    Create a file if it does not exists.
    Remove if the file exists and then create it again.

    Parameters
    ----------
    file_path : str
        location to create the file
    """
    if os.path.exists(file_path) and remove_if_exists:
        os.remove(file_path)
    try:
        with open(file_path, "x", encoding="utf8"):
            pass
    except FileExistsError:
        pass


def get_filename_without_extension(filename, file_extension=".survey"):
    """For files of the pattern name.ext, get the name part.

    Parameters
    ----------
    filename : str
        Has the expected format name.ext
    file_extension : str
        extension string, by default ".survey"

    Returns
    -------
    str
        returns the name part of a filename
    """
    name_wo_extension, _ = filename.split(file_extension)
    name = utils.convert_filename(name_wo_extension, file_or_console=False)
    return name


def convert_filename(name, file_or_console=True):
    """
    Convert names with whitespaces to _ separated names and vice versa

    Parameters
    ----------
    name : str
        target name
    file_or_console : bool, optional
        deciding if the name is for filename or console name,
        by default True indicating filename

    Returns
    -------
    str
        changed name
    """
    if file_or_console:  # change to _ separated variable for filename
        changed_name = "_".join(name.split())
    else:  # change to whitespace separated variable for console
        changed_name = " ".join(_.capitalize() for _ in name.split("_"))
    return changed_name


def safe_integer_input(valid_range,
                       text_prompt="Enter your choice: ",
                       num_retries=3):
    """
    Handles incorrectly provided options

    Parameters
    ----------
    valid_range : list
        range of values for valid options
    text_prompt: str
        prompt to show while collecting user input
    num_retries : int
        number of times a wrong option can be provided. Defaults to 3.

    Raises:
        ValueError: if wrong option is provided

    Returns:
        int
    """
    error_text_terminate = "You have no more trials left. Exiting...!"

    option = None
    for attempt_no in range(num_retries):
        try:
            option = int(input(text_prompt))
        except ValueError:
            print("Please provide correct integer choice!")
            continue

        if option not in valid_range:
            remaining_trials = num_retries-attempt_no-1

            if remaining_trials == 0:
                print(error_text_terminate)
                return None

            error_text = f"You have {remaining_trials} more trials!"
            print(f"Not a valid option. Please try again! {error_text}")

        else:
            return option

    return option
