import pathlib
import requests_mock
import os
import sys
import tempfile
from page_loader import download
from urllib.parse import urljoin

URL = 'https://ru.hexlet.io/courses'
DIR_NAME = 'ru-hexlet-io-courses_files'
RESOURCES_URL = [urljoin(URL, '/assets/professions/nodejs.png')]

EXPECTED_CONTENT = RESOURCES_URL[:]

with open(pathlib.PurePath(sys.path[0], 'fixtures/after.html'), 'r') as file:
    expected_page = file.read()


def test_download():
    with open(pathlib.PurePath(sys.path[0], 'fixtures/before.html'),
              'r') as f:
        testing_page = f.read()
    with tempfile.TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text=testing_page)
            [m.get(url, text=content) for url, content
             in zip(RESOURCES_URL, EXPECTED_CONTENT)]
            file_path = download(URL, tmp_dir)
            with open(file_path, 'r') as file:
                page = file.read()
            assert len(os.listdir(tmp_dir)) == 1
            assert len(os.listdir(pathlib.PurePath(tmp_dir, DIR_NAME))) == 3
            assert page == expected_page
