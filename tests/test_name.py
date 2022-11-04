from page_loader.name import remove_schema, remove_extra_symbols, get_html_name

URL = 'http://test.com/'
URL_2 = 'https://test.com/'
URL_3 = 'test.com/'


def test_remove_schema():
    assert 'test.com/' == remove_schema(URL)
    assert 'test.com/' == remove_schema(URL_2)
    assert 'test.com/' == remove_schema(URL_3)


def test_remove_extra_symbols():
    assert 'http://test.com' == remove_extra_symbols(URL)
    assert 'https://test.com' == remove_extra_symbols(URL_2)
    assert 'test.com' == remove_extra_symbols(URL_3)


def test_get_html_name():
    assert 'test-com.html' == get_html_name(URL)
    assert 'test-com.html' == get_html_name(URL_2)
    assert 'test-com.html' == get_html_name(URL_3)
