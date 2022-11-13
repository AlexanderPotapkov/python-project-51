from os import mkdir
from os.path import exists

from page_loader.logger import get_logger

logger = get_logger(__name__)


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
        logger.exception(f'File not saved. Error: {expt}')
        raise FileNotFoundError(f'File not saved. Error: {expt}')
    except TypeError as expt:
        logger.exception(f'File not saved. Error: {expt}')
    logger.info(f'File {file_path} saved.')


def mk_dir(output):
    """
    :param output: path and dir name
    :return: None
    """
    if not exists(output):
        try:
            mkdir(output)
        except OSError:
            logger.error('Failed to create resource folder.')
            raise FileNotFoundError('Failed to create resource folder.')
