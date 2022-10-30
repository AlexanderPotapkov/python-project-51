import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.namer import get_dir_name, get_file_name, get_img_name


def is_valid_url(url):
    parsed = urlparse(url)

    return bool(parsed.netloc) and bool(parsed.scheme)


def get_images(new_folder, soup):
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    for res in soup.findAll('img'):
        filename = os.path.basename(res['src'])
        filepath = os.path.join(new_folder, get_img_name(filename))
        res['src'] = os.path.join(os.path.basename(new_folder), get_img_name(filename))
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
            print(filepath)

    return soup


def download(url, output):
    if is_valid_url(url):
        response = requests.Session().get(url)
        save_file = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        new_dir = get_dir_name(url, output)
        soup = get_images(new_dir, soup)
        with open(get_file_name(url, output), 'w', encoding='utf-8') as f:
            if not os.path.isfile(soup.prettify()):
                f.write(soup.prettify())

    return f'{get_dir_name(url, output)}\n' f'{get_file_name(url, output)}'
