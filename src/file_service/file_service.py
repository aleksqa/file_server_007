from typing import Optional, List, Union
from src import utils
import os


def unique_file_name() -> str:
    """
    Generate unique file name

    :return: unique file name
    """
    while True:
        name = utils.random_string()
        if not os.path.exists(name):
            return name


def create_file(content: str) -> str:
    """
    Create new file with unique name and content inside

    :param content: some input to be added to file
    :return: file name with content
    """
    filename = unique_file_name()
    with open(filename, "w") as file:
        file.write(content)
    return filename


def delete_file(filename: str) -> bool:
    """
    Remove file by name

    :param filename: file name to be deleted
    :return: None
    """
    if check_file(filename):
        os.remove(filename)
        return True
    return False


def list_dir() -> list[str]:
    """
    Get list of files and directories

    :return: list of files and directories
    """
    ls = os.listdir()
    # for file in ls:
    #     print(file)
    return ls


def change_dir(directory: str) -> bool:
    """
    Change directory

    :param directory: name of dir to switch
    :return: True if dir exist, False otherwise
    """
    if check_dir(directory):
        os.chdir(directory)
        return True
    return False


def read_file(filename: str) -> Optional[str]:
    """
    Read file by name

    :param filename: file name to be read
    :return: file name
    """
    if check_file(filename):
        with open(filename, "r") as f:
            return f.read()
    else:
        return None


def check_file(filename: str) -> bool:
    """
    Check file exists

    :param filename: name of file
    :return: boolean value
    """
    return os.path.isfile(filename)


def check_dir(directory: str) -> bool:
    """
    Checks if directory exist
    :param directory path to directory to check
    :returns True if directory exists
    """
    return os.path.isdir(directory)


# def get_file_permissions(filename: str) -> Optional[str]:
#     """
#     Gets file permissions in hex
#     :param filename name of file
#     :returns hex number
#     """
#     if check_file(filename):
#         return hex(os.stat(filename).st_mode)
#     else:
#         return None
#
#
# def set_file_permissions(filename: str, permissions: str):
#     """
#     Sets file permissions
#     :param filename name of file
#     :param permissions hex number
#     :returns True if permissions set
#     """
#     if check_file(filename):
#         os.chmod(filename, int(permissions, 16))
#         return True
#     else:
#         return False

def get_file_meta_data(filename: str) -> Union[tuple, bool]:
    """
    Read file creation date, modification date, size of file

    :param filename: file to read
    :return: tuple (create_date, modification_date, filesize)
    """
    if check_file(filename) and not (check_dir(filename)):
        stat = os.stat(filename)
        return stat.st_ctime, stat.st_mtime, stat.st_size
    else:
        return False
