from os.path import basename
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.namer import get_file_name

from page_loader.logger import get_logger

logger = get_logger(__name__)


def download_resources(url, text_html, resource_dir):
    """
    :param resource_dir: dir for downloaded resources
    :param url: url address
    :param text_html: html-text
    :return: modified html-text and resource list
    """
    tags = [
        {'tag': 'img', 'attr': 'src'},
        {'tag': 'link', 'attr': 'href'},
        {'tag': 'script', 'attr': 'src'},
    ]
    html_page = urlparse(url)
    soup = BeautifulSoup(text_html, 'html.parser')

    resources_list = []
    for tag in tags:
        for element in soup.find_all(tag['tag']):
            logger.debug(f'Checked: {element}')
            url = element.attrs.get(tag['attr'])
            if url is None:
                continue
            url = urlparse(url)
            if url.netloc != html_page.netloc and url.netloc != '':
                logger.debug('Link to another domain.')
                continue

            url = f'{html_page.scheme}://{html_page.netloc}{url.path}'
            file_name = get_file_name(url)
            element[tag['attr']] = f'{basename(resource_dir)}/{file_name}'

            resources_list.append(
                {
                    'link': url,
                    'path': element[tag['attr']],
                },
            )
    return resources_list, soup.prettify()
