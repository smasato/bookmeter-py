from bs4 import BeautifulSoup
import requests
from .__version__ import __version__


def get(url):
    headers = {
        'User-Agent': 'bookmeter-py v{}'.format(__version__)
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')

    return soup
