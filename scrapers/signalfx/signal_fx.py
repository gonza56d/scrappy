# Project
from pages import SignalFxPage
from scrapers.base_scraper import BaseScraper


class SignalFxScrapper(BaseScraper):

    page_class = SignalFxPage
    headers = ['name', 'company_text', 'company_link', 'role', 'sweet_spot', 'range', 'investments', 'categories']

    def __init__(self, executable_path):
        self.page = self.page_class(executable_path)
        super().__init__(self.page, self.headers)
