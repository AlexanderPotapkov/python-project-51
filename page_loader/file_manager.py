import logging

from os import mkdir
from os.path import exists


def save_file(file_path, content):
    """
    :param file_path: path and file name
    :param content: file content
    :return: None
    """
    flag = 'w' if isinstance(content, str) else 'wb'
    try:
        with open(file_path, flag) as res_file:
            res_file.write(content)
    except FileNotFoundError as expt:
        logging.exception(f'File not saved. Error: {expt}')
        raise FileNotFoundError(f'File not saved. Error: {expt}')
    except TypeError as expt:
        logging.exception(f'File not saved. Error: {expt}')
    logging.info(f'File {file_path} saved.')


def mk_dir(output):
    """
    :param output: path and dir name
    :return: None
    """
    if not exists(output):
        try:
            mkdir(output)
        except OSError:
            logging.error('Failed to create resource folder.')
            raise FileNotFoundError('Failed to create resource folder.')
