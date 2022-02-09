import argparse
import os
import yaml

from src import file_service
import logging
import logging.config


with open(file="./logging_config.yaml", mode='r') as file:
    logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)


def read_file():
    logging.info("read_file() is called")
    filename = input("Enter file name : ")
    file_service.read_file(filename)


def create_file():
    logging.info("create_file() is called")
    content = input("Enter file content : ")
    file_service.create_file(content=content)


def delete_file():
    logging.info("delete_file() is called")
    filename = input("Enter file name : ")
    file_service.delete_file(filename)


def list_dir():
    logging.info("list_dir() is called")
    file_service.list_dir()


def change_dir():
    logging.info("change_dir() is called")
    directory = input("Enter dir name : ")
    file_service.change_dir(directory)


def get_metadata():
    logging.info("get_metadata() is called")
    filename = input("Enter file name : ")
    file_service.get_file_meta_data(filename)


def main():
    logging.getLogger("telemetry").info("Application is running")
    parser = argparse.ArgumentParser(description='Restfull file server')
    parser.add_argument('-d', '--directory', help='Current directory', default='C:/IdeaProjects/Luxoft/file_server_007')
    args = parser.parse_args()
    os.chdir(args.directory)
    commands = {
        "get": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir,
        "meta": get_metadata
    }
    while True:
        command = input("Enter command: ")
        if command == "exit":
            logging.getLogger("telemetry").info("Application is stopped")
            return
        if command not in commands:
            logging.error("Unknown command")
            print("Unknown command")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution : {ex}")


if __name__ == "__main__":
    main()
