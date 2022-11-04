import re

from urllib.parse import urlparse


def remove_schema(url):
    """
    :param url: website address
    :return: URL without schema
    """
    parsed_url = urlparse(url)

    return parsed_url.netloc + parsed_url.path


def remove_extra_symbols(url):
    """
    :param url: website address
    :return: URL without '/' in the end of the path
    """
    if url.endswith('/'):
        url = url[:-1]
    if not url[0].isalnum():
        url = url[1:]

    return url


def get_html_name(url):
    """
    :param url: website address
    :return: name for download HTML file
    """
    filename = re.sub(r'[^a-zA-Z0-9]', '-', remove_schema(remove_extra_symbols(url)))

    return f'{filename}.html'
