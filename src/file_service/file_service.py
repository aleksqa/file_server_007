from src import utils
import os


def unique_file_name():
    name = utils.random_string()
    return name


def create_file(content):
    filename = unique_file_name()
    while os.path.exists(filename):
        filename = unique_file_name()
    with open(filename, "w") as file:
        file.write(content)
    return filename


def delete_file(filename):
    if not os.path.isfile(filename):
        print("This is not a file")
        return
    os.remove(filename)


def list_dir():
    ls = os.listdir()
    for file in ls:
        print(file)
    return ls


def read_file(filename):
    if not os.path.isfile(filename):
        print("This is not a file")
        return
    with open(filename, "r") as f:
        data = f.read()
    return data


def change_dir(directory):
    if not os.path.isdir(directory):
        print("is not a directory")
        return
    os.chdir(directory)


