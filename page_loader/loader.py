import logging
import requests

from os.path import abspath, join
from progress.bar import Bar
from urllib.parse import urlparse

from page_loader.file_manager import mk_dir, save_file
from page_loader.web_manager import download_resources
from page_loader.namer import get_file_name, get_dir_name


def get_content(url):
    """
    :param url: url address
    :return: url content
    """
    if not urlparse(url).netloc:
        raise ValueError('Incomplete address.')

    try:
        response = requests.get(url)
    except requests.RequestException as expt:
        logging.error(f'Connection error: {expt}')
        raise ConnectionError(f'Connection error: {expt}')
    if response.status_code != requests.codes.ok:
        logging.error(f'Link unavailable. {response.status_code}')
        raise ConnectionError(f'Link unavailable. {response.status_code}')
    logging.info(f'File {url} received.')
    conn_type = response.headers.get('Content-Type')
    if conn_type and 'text/html' in conn_type:
        response.encoding = 'utf-8'
        return response.text
    else:
        return response.content


def download(url, output):
    """
    :param url: url address
    :param output: output dir for save files
    :return: full path to download files
    """

    path_name = get_file_name(url)
    path_name = join(output, path_name)
    dir_name = get_dir_name(url, output)

    text_html = get_content(url)
    urls, text_html = download_resources(url, text_html, dir_name)

    save_file(path_name, text_html)

    mk_dir(dir_name)
    progress_bar = Bar('Saving: ', max=len(urls))
    for url in urls:
        try:
            resources = get_content(url['link'])
            save_file(join(output, url['path']), resources)
        except ConnectionError as expt:
            logging.debug(f'Resource {url} is not loaded. {expt}')
            continue
        except OSError:
            logging.info(f'Resource {url} is not saved.')
            progress_bar.next()
            continue
        logging.info(f'Resource {url} saved.')
        progress_bar.next()
    progress_bar.finish()

    return abspath(path_name)
