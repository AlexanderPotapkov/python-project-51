import pytest


@pytest.fixture()
def text_html():
    with open('tests/fixtures/test.html', 'r') as test_page:
        text = test_page.read()
    return text


@pytest.fixture()
def img_content():
    with open('tests/fixtures/img/python.png', 'rb') as img_file:
        content = img_file.read()
    return content


@pytest.fixture()
def css_content():
    with open('tests/fixtures/files/css/style.css', 'rb') as css_file:
        content = css_file.read()
    return content


@pytest.fixture()
def js_content():
    with open('tests/fixtures/empty.js', 'rb') as js_file:
        content = js_file.read()
    return content
