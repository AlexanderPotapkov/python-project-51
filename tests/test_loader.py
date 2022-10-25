import pathlib
import requests_mock
import sys
import tempfile
from page_loader import download

URL = 'https://ru.hexlet.io/courses'

with open(pathlib.PurePath(sys.path[0], 'fixtures/ru-hexlet-io-courses.html'), 'r') as file:
    expected_page = file.read()


def test_download():
    with open(pathlib.PurePath(sys.path[0], 'fixtures/ru-hexlet-io-courses.html'),
              'r') as f:
        testing_page = f.read()
    with tempfile.TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text=testing_page)
            file_path = download(URL, tmp_dir)
            with open(file_path, 'r') as f:
                page = f.read()
            assert page == expected_page
