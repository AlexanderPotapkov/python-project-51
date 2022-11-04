import os
import requests

from page_loader.name import get_html_name


def download(url, output):
    """
    :param url: URL address
    :param output: path to download files
    :return: full path to download files
    """
    response = requests.get(url)
    file_name = get_html_name(url)
    file_name = os.path.join(output, file_name)
    with open(file_name, 'w') as html_file:
        html_file.write(response.text)

    return os.path.abspath(file_name)
