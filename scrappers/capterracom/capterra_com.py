
# Pages
from pages import CapterraComPage
from scrappers.base_scrapper import BaseScrapper


class CapterraComScrapper(BaseScrapper):
    """Implementation of CapterraComPage"""

    page_class = CapterraComPage
    headers = ['name', 'url']

    def __init__(self, executable_path):
        self.page = self.page_class(executable_path)
        super().__init__(self.page, self.headers)
