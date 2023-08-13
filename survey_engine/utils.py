
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
