import os

def check_folders(folder_name, file_name):
    """
    Check if the folder exists, and create it if it doesn't.
    Parameters
    ----------
    folder_name : str
        The folder name to check or create.
    file_name : str
        The name of the file.
    Returns
    -------
    str
        The full file path.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, file_name)
    return file_path
