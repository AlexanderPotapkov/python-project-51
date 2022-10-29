import re


def get_file_name(url, output):
    if url.startswith('http:'):
        filename = re.sub(r'\W', '-', url[7::])
    elif url.startswith('https:'):
        filename = re.sub(r'\W', '-', url[8::])
    return f'{output}/{filename}.html'


def get_dir_name(url, output):
    if url.startswith('http:'):
        filename = re.sub(r'\W', '-', url[7::])
    elif url.startswith('https:'):
        filename = re.sub(r'\W', '-', url[8::])
    return f'{output}/{filename}_files'
