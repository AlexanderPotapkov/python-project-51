import os


def create_dir_for_files(path_to_files_dir):
    os.mkdir(path_to_files_dir)


def save_file(path, data):
    flag = 'wb' if is_bytes(data) else 'w'
    with open(path, flag) as file:
        file.write(data)


def check_output_dir(path):
    return os.path.exists(path)


def is_bytes(data):
    return isinstance(data, bytes)
