from page_loader.loader import download, change_url, remove_schema
from unittest.mock import Mock


def test_download():
    mock = Mock()
    expect = '''/Users/alexander_potapkov/PycharmProjects/python-project-51/tmp/ru-hexlet-io-courses.html'''
    assert download('https://ru.hexlet.io/courses', '/tmp') == expect

def test_change_url():
    expect = 'ru-hexlet-io-courses.html'
    assert change_url('https://ru.hexlet.io/courses') == expect

def tets_remove_schema():
    assert remove_schema('https://site.com') == 'site.com'
    assert remove_schema('http://site.com') == 'site.com'
    assert remove_schema('site.com') == 'site.com'
