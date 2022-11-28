import requests_mock

from page_loader.html import gathering_resources
from page_loader.loader import get_content


RAW = 'tests/fixtures/test.html'
HTML = 'tests/fixtures/expected.html'
URL = 'https://www.test.com'
EXPECTED_DIR_NAME = 'www-test-com_files'

def read(file, binary=False):
    if not binary:
        with open(file, 'r') as f:
            return f.read()
    with open(file, 'rb') as file:
        return file.read()


def test_gathering_resources():
    html_raw = read(RAW)
    html_expected = read(HTML)

    with requests_mock.Mocker() as m:
        m.get(URL, text=html_raw)
        response = get_content(URL)
        resources, processed_html = gathering_resources(URL, response, EXPECTED_DIR_NAME)

        expected_resources = [{'link': 'https://www.test.com/img/python.png',
                               'path': 'www-test-com_files/www-test-com-img-python.png'},
                              {'link': 'https://www.test.com/files/css/style.css',
                               'path': 'www-test-com_files/www-test-com-files-css-style.css'},
                              {'link': 'https://www.test.com/empty.js',
                               'path': 'www-test-com_files/www-test-com-empty.js'}
                              ]

        assert processed_html == html_expected
        assert resources == expected_resources
