# Project
from pages import G2ComPage
from scrapers.base_scraper import BaseScraper


class G2ComScraper(BaseScraper):
    """Implementation of G2ComPage"""

    page_class = G2ComPage
    headers = ['name', 'url', 'description']

    def __init__(self, executable_path):
        self.page = self.page_class(executable_path)
        super().__init__(self.page, self.headers)

