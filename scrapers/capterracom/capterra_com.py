# Project
from pages import CapterraComPage
from scrapers.base_scraper import BaseScraper


class CapterraComScraper(BaseScraper):
    """Implementation of CapterraComPage"""

    page_class = CapterraComPage
    headers = ['name', 'url', 'description', 'by']

    def __init__(self, executable_path):
        self.page = self.page_class(executable_path)
        super().__init__(self.page, self.headers)
