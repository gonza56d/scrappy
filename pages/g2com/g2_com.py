"""https://www.g2.com/categories/sales-analytics"""

# Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Project
from pages import BasePage


class G2ComPageRow(WebElement):
    pass


class G2ComPage(BasePage):

    by_row = (By.CLASS_NAME, 'product-listing')
    page_url = 'https://www.g2.com/categories/sales-analytics'
    page_row_class = G2ComPageRow

    def __init__(self, executable_path):
        super().__init__(executable_path, self.page_url, self.by_row, self.page_row_class)
