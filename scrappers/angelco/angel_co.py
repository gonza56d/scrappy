"""Implementation of AngelCoPage"""

# Project
from pages import AngelCoPage
from scrappers.base_scrapper import BaseScrapper


class AngelCoScrapper(BaseScrapper):

    page_class = AngelCoPage
    headers = ['name', 'description', 'location', 'area', 'investments', 'followers']

    def __init__(self, executable_path):
        self.page = self.page_class(executable_path)
        super().__init__(self.page, self.headers)
