from urllib.parse import urlparse

BASE_URL = "https://bookmeter.com/"


def _checkUrl(url):
    base = urlparse(BASE_URL)
    o = urlparse(url)

    if base.scheme == o.scheme and base.netloc == o.netloc:
        return True
    else:
        return False


class Bookmeter:
    def __init__(self, url):
        self.url = url

    def scraping(self, url):
        if not _checkUrl(url):
            return None

    def users(self):
        pass

    def books(self):
        pass

    def is_valid(self):
        return _checkUrl(self.url)

    def path(self):
        o = urlparse(self.url)
        return o.path[1:].split('/')
