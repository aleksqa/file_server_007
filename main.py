import argparse
import os
from src import file_service


def read_file():
    filename = input("Enter file name : ")
    file_service.read_file(filename)


def create_file():
    content = input("Enter file content : ")
    file_service.create_file(content=content)


def delete_file():
    filename = input("Enter file name : ")
    file_service.delete_file(filename)


def list_dir():
    file_service.list_dir()


def change_dir():
    directory = input("Enter dir name : ")
    file_service.change_dir(directory)


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
