import logging

from os.path import basename
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.namer import get_file_name


def is_domain(url, html_page):
    return url.netloc != html_page.netloc and url.netloc != ''


def gathering_resources(url, text_html, resource_dir):
    """
    :param resource_dir: dir for downloaded resources
    :param url: url address
    :param text_html: html-text
    :return: modified html-text and resource list
    """
    tags = {'img': 'src',
            'link': 'href',
            'script': 'src'}

    html_page = urlparse(url)
    soup = BeautifulSoup(text_html, 'html.parser')

    resources_list = []
    for tag, attr in tags.items():
        for element in soup.find_all(tag):
            logging.debug(f'Checked: {element}')
            url = element.attrs.get(attr)
            if url is None:
                continue
            url = urlparse(url)
            if is_domain(url, html_page):
                logging.debug('Link to another domain.')
                continue

            url = f'{html_page.scheme}://{html_page.netloc}{url.path}'
            file_name = get_file_name(url)
            if element is not None:
                element[attr] = f'{basename(resource_dir)}/{file_name}'

                resources_list.append(
                    {
                        'link': url,
                        'path': element[attr],
                    },
                )
    return resources_list, soup.prettify()
