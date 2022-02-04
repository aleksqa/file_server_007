import argparse
import os
import random
import string


def rnd_name():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def read_file():
    filename = input("Enter file name : ")
    if not os.path.exists(filename):
        print("File does not exist")
        return
    if not os.path.isfile(filename):
        print("This is not a file")
        return
    with open(filename, "r") as f:
        data = f.read()
        print(data)


def create_file():
    filename = rnd_name()
    content = input("Enter file content : ")
    with open(f"{filename}.txt", "w") as f:
        f.write(content)
    print('File {}.txt was created'.format(filename))


def delete_file():
    filename = input("Enter file name : ")
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


def change_dir():
    directory = input("Enter dir name : ")
    if not os.path.exists(directory):
        print("Directory is not exist")
        return
    if not os.path.isdir(directory):
        print("is not a directory")
        return
    os.chdir(directory)
    print('Current directory: {}'.format(directory))


def main():
    parser = argparse.ArgumentParser(description='Restfull file server')
    parser.add_argument('-d', '--directory', help='Current directory', default='C:/IdeaProjects/Luxoft/file_server_007')
    args = parser.parse_args()
    os.chdir(args.directory)
    commands = {
        "get": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir
    }
    while True:
        command = input("Enter command: ")
        if command == "exit":
            return
        if command not in commands:
            print("Unknown command")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution : {ex}")


if __name__ == "__main__":
    main()
