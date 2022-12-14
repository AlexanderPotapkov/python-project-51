import re
import string

from urllib.parse import urlparse


def remove_schema(url):
    '''
    :param url:  url address
    :return: url without schema
    '''
    parsed_url = urlparse(url)
    return parsed_url.netloc + parsed_url.path


def remove_extra_symbols(url):
    '''
    :param url:   url address
    :return: url without "/" in the end of string
    '''
    if url.endswith('/'):
        url = url[:-1]
    if not url[0].isalnum():
        url = url[1:]
    return url


def to_filename(url):
    """
    :param url: url address
    :return: new file name
    """
    netloc = urlparse(remove_extra_symbols(url)).netloc
    path = urlparse(remove_extra_symbols(url)).path
    if path:
        path = path if path[0] == '/' else f'/{path}'
    file_name = path.split('/')[-1]
    if path and '.' in file_name:
        ext = file_name.split('.')[-1]
        file_name = f'{path[:-(len(ext) + 1)]}'
    else:
        file_name = path
        ext = 'html'
    file_name = f'{netloc}{file_name}' if netloc else f'{file_name[1:]}'
    alpha_num = string.ascii_letters + string.digits
    file_name = [char if char in alpha_num else '-' for char in file_name]
    file_name = ''.join(file_name)
    return f'{file_name}.{ext}'


def to_dirname(url, output):
    filename = re.sub(r'\W', '-', remove_schema(remove_extra_symbols(url)))
    return f'{output}/{filename}_files'
