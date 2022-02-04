from src import utils
import os


def unique_file_name():
    name = utils.random_string()
    return name


def create_file(content):
    filename = unique_file_name()
    with open(f"{filename}.txt", "w") as file:
        file.write(content)
    print('File {}.txt was created with content {}'.format(filename, content))


def delete_file(filename):
    if not os.path.exists(filename):
        print("File does not exist")
        return
    if not os.path.isfile(filename):
        print("This is not a file")
        return
    os.remove(filename)
    print("File {} was deleted".format(filename))


def list_dir():
    ls = os.listdir()
    for file in ls:
        print(file)


def read_file(filename):
    if not os.path.exists(filename):
        print("File does not exist")
        return
    if not os.path.isfile(filename):
        print("This is not a file")
        return
    with open(filename, "r") as f:
        data = f.read()
        print(data)


def change_dir(directory):
    if not os.path.exists(directory):
        print("Directory is not exist")
        return
    if not os.path.isdir(directory):
        print("is not a directory")
        return
    os.chdir(directory)
    print('Current directory: {}'.format(directory))