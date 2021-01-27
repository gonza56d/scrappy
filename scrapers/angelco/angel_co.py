# Project
from pages import AngelCoPage
from scrapers.base_scraper import BaseScraper


class AngelCoScraper(BaseScraper):
    """Implementation of AngelCoPage"""

    page_class = AngelCoPage
    headers = ['name_plus_link', 'description', 'location', 'area', 'investments', 'followers']

    def __init__(self, executable_path):
        self.page = self.page_class(executable_path)
        super().__init__(self.page, self.headers)
