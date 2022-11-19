import pytest
import requests_mock

from os import listdir
from os.path import exists, join
from tempfile import TemporaryDirectory

from page_loader.loader import download
from page_loader.namer import get_file_name

EXPECTED_FILE_NAME = 'www-test-com.html'
EXPECTED_DIR_NAME = 'www-test-com_files'
URL = 'https://www.test.com'
IMG_PATH = f'{URL}/img/python.png'
CSS_PATH = f'{URL}/files/css/style.css'
JS_PATH = f'{URL}/empty.js'

HEAD_TXT = {'Content-Type': 'text/html'}
HEAD_ALL = {'Content-Type': 'all'}


def test_page_loader_download(
        text_html,
        img_content,
        css_content,
        js_content
):
    indicator = False

    with TemporaryDirectory() as temp_dir:
        expected_path = join(temp_dir, EXPECTED_FILE_NAME)
        with requests_mock.Mocker() as mock:
            mock.get(URL, text=text_html, headers=HEAD_TXT)
            mock.get(IMG_PATH, content=img_content, headers=HEAD_ALL)
            mock.get(CSS_PATH, content=css_content, headers=HEAD_ALL)
            mock.get(JS_PATH, content=js_content, headers=HEAD_ALL)
            received_path = download(URL, temp_dir)
        if exists(received_path) and exists(join(temp_dir, EXPECTED_DIR_NAME)):
            indicator = True

    current_file_name = received_path.split('/')[-1]

    assert expected_path == received_path
    assert indicator
    assert EXPECTED_FILE_NAME == current_file_name


def test_page_loader_files(
        text_html,
        img_content,
        css_content,
        js_content
):
    with open('tests/fixtures/expected.html', 'r') as exp_file:
        expected = exp_file.read()

    with TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as mock:
            mock.get(URL, text=text_html, headers=HEAD_TXT)
            mock.get(IMG_PATH, content=img_content, headers=HEAD_ALL)
            mock.get(CSS_PATH, content=css_content, headers=HEAD_ALL)
            mock.get(JS_PATH, content=js_content, headers=HEAD_ALL)
            received_patch = download(URL, temp_dir)
        with open(received_patch, 'r') as file_html:
            received = file_html.read()

        path = join(temp_dir, EXPECTED_DIR_NAME)
        list_file = listdir(path)
        list_content = {img_content, css_content, js_content}
        exp_list_content = set()
        for item in list_file:
            with open(join(path, item), 'rb') as f:
                exp_list_content.add(f.read())

    assert len(list_file) == 3
    assert expected == received
    assert exp_list_content == list_content


def test_page_loader_exceptions():
    with TemporaryDirectory() as temp_dir:
        with pytest.raises(FileNotFoundError):
            download('https://google.com', 'wrong_folder')

        with pytest.raises(ConnectionError):
            download('wrong_site.', temp_dir)

        with pytest.raises(ConnectionError):
            with requests_mock.Mocker() as mock:
                mock.get('https://google.com', status_code=404)
                download('https://google.com', temp_dir)


def test_page_loader_link_to_filename():
    list_link = [
        'https://site.com',
        'https://site.com/asdf/fer',
        'https://site.com/asdf/fer.png',
        '/site/asdf/fer.png',
        'site/asdf/fer',
    ]
    expected_list_link = [
        'site-com.html',
        'site-com-asdf-fer.html',
        'site-com-asdf-fer.png',
        'site-asdf-fer.png',
        'site-asdf-fer.html',
    ]
    for index, link in enumerate(expected_list_link):
        assert get_file_name(list_link[index]) == link, list_link[index]
