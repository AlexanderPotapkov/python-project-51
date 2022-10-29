import os
import pathlib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.namer import get_dir_name, get_file_name


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# def get_images(url: str) -> list:
#    html = requests.get(url).text
#    soup = BeautifulSoup(html, "html.parser")


def download(url: str, output: str = pathlib.Path.cwd()) -> str:
    save_file = requests.request('GET', url).text
    with open(get_file_name(url, output), 'w', encoding='utf-8') as f:
        if not os.path.isfile(save_file):
            f.write(save_file)
    if not os.path.isdir(get_dir_name(url, output)):
        os.mkdir(get_dir_name(url, output))
    return f'{get_dir_name(url, output)}\n' f'{get_file_name(url, output)}'
