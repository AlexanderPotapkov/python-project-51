"""Main module"""
import requests
from page_loader.loader import download

__all__ = ('download',)


class PageLoadingError(requests.exceptions.HTTPError):
    def __init__(self, error_message):
        self.error_message = error_message
