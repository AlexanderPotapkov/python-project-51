import pytest


@pytest.fixture()
def text_html():
    with open('tests/fixtures/test.html', 'r') as test_page:
        text = test_page.read()
    return text


@pytest.fixture()
def img1_content():
    with open('tests/fixtures/img/python.png', 'rb') as img_fle:
        content = img_fle.read()
    return content


@pytest.fixture()
def css_content():
    with open('tests/fixtures/files/css/style.css', 'rb') as css_fle:
        content = css_fle.read()
    return content


@pytest.fixture()
def js_content():
    with open('tests/fixtures/empty.js', 'rb') as js_fle:
        content = js_fle.read()
    return content
