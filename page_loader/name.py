import os
from pathlib import PurePath, PurePosixPath
from urllib.parse import urljoin, urlparse


def get_path(path, name):
    return PurePath(path, name)


def get_absolute_url(main_url, url):
    return urljoin(main_url, url)


def remove_scheme(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc + parsed_url.path


def remove_extra_symbols(url):
    if url.endswith('/'):
        url = url[:-1]
    if not url[0].isalnum():
        url = url[1:]
    return url


def get_url_without_dashes(url):
    new_url = []
    for symbol in url:
        if not symbol.isalnum():
            new_url.append('-')
        else:
            new_url.append(symbol)
    return ''.join(new_url)


def get_html_name(url):
    filename = get_url_without_dashes(remove_scheme(remove_extra_symbols(url)))

    return filename + '.html'


def get_dir_name(url):
    filename = get_url_without_dashes(remove_scheme(remove_extra_symbols(url)))

    return filename + '_files'


def get_file_name(url):
    name = []
    new_url = remove_scheme(remove_extra_symbols(url))
    if PurePosixPath(new_url):
        new_url, suffix = os.path.splitext(new_url)
        name.append(get_url_without_dashes(new_url))
        name.append(suffix)
    return ''.join(name)


def get_name_from_tag(tag_object):
    tag_object.name = 'img'
    return tag_object.get('src'), tag_object.name
