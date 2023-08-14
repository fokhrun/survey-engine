
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
