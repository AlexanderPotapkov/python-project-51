import re
from urllib.parse import urlparse
from pathlib import Path


def remove_scheme(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc + parsed_url.path


def get_file_name(url, output):
    filename = re.sub(r'[^a-zA-Z0-9]', '-', remove_scheme(url))

    return f'{output}/{filename}.html'


def get_dir_name(url, output):
    filename = re.sub(r'[^a-zA-Z0-9]', '-', remove_scheme(url))

    return f'{output}/{filename}_files'


def get_img_name(filename):
    path = Path(filename)
    img_name = re.sub(r'[^a-zA-Z0-9]', '-', str(path.with_suffix('')))

    return f'{img_name}.png'
