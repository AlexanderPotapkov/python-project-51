import os.path
import requests_mock

from tempfile import TemporaryDirectory

from page_loader.loader import download


def test_download():
    file_presence = False
    expected_page_name = 'www-test-com.html'
    url = f'https://www.test.com'

    with open(f'tests/fixtures/{expected_page_name}', 'r') as test_html:
        text_html = test_html.read()

    with TemporaryDirectory() as temp_dir:
        expected_patch = os.path.join(temp_dir, expected_page_name)
        with requests_mock.Mocker() as mock:
            mock.get(url, text=text_html)
            received_patch = download(url, temp_dir)
        if os.path.exists(received_patch):
            file_presence = True

    current_name = received_patch.split('/')[-1]

    assert expected_patch == received_patch
    assert file_presence
    assert expected_page_name == current_name
