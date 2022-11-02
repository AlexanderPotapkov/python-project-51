import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from page_loader.change import change_path
from page_loader.file_manager import save_file
from page_loader.name import get_file_name, get_absolute_url, get_path, get_name_from_tag


def get_response(url):
    return requests.get(url)


def get_soup(response):
    return BeautifulSoup(response.content, 'html.parser')


def is_proper_to_download(base_url, tag_url):
    base_url_host = urlparse(base_url).netloc
    tag_url_host = urlparse(tag_url).netloc
    return (not ((not tag_url or not (tag_url != base_url) or not (tag_url_host in base_url_host)) and tag_url_host))


def download_resources(url, parsed_data, get_dir_name):
    resources = parsed_data.find_all(['img'])
    for resource_tag in resources:
        if get_name_from_tag(resource_tag) is None:
            continue
        tag_url, tag_name = get_name_from_tag(resource_tag)
        absolute_url = get_absolute_url(url, tag_url)
        if not is_proper_to_download(url, tag_url):
            continue
        file_name = get_file_name(absolute_url)
        file_path = get_path(get_dir_name, file_name)
        resource_response = get_response(absolute_url)
        resource_content = resource_response.content
        save_file(file_path, resource_content)
        change_path(resource_tag, tag_name, file_path)
