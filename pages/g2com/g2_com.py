"""https://www.g2.com/categories/sales-analytics"""

# Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Project
from pages import BasePage


class G2ComPageRow(WebElement):

    by_name = (By.XPATH, './/div[@itemprop="name"]')
    by_url = (By.CLASS_NAME, 'd-ib.c-midnight-100.js-log-click')
    by_description = (By.CLASS_NAME, 'product-listing__paragraph.x-truncate-revealer-initialized')

    def __init__(self, web_element):
        super().__init__(*tuple(web_element.__dict__.values()))

    @property
    def name(self):
        return self.find_element(*self.by_name).text

    @property
    def url(self):
        return self.find_element(*self.by_url)

    @property
    def description(self):
        return self.find_element(*self.by_description)


class G2ComPage(BasePage):

    by_row = (By.CLASS_NAME, 'product-listing')
    page_url = 'https://www.g2.com/categories/sales-analytics'
    page_row_class = G2ComPageRow

    def __init__(self, executable_path):
        super().__init__(executable_path, self.page_url, self.by_row, self.page_row_class)
