
"""Utility functions"""

import os


def create_file_safely(file_path):
    """
    Create a file if it does not exists. Remove if the file exists and then create it again.

    Parameters
    ----------
    file_path : str
        location to create the file
    """
    if os.path.exists(file_path):
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
    return name_wo_extension
