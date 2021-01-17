"""https://www.capterra.com/architecture-software/"""

# Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Project
from pages import BasePage


class CapterraComPageRow(WebElement):

    by_name = (By.XPATH, './/a[@cllass="ProductHeaderSection__ProductHeaderLink-sc-55o1a3-1 nlUij Link__StyledStandardLink-e9c1rj-0 eZMnyW"][1]//span')
    by_url = (By.XPATH, './/a[@cllass="ProductHeaderSection__ProductHeaderLink-sc-55o1a3-1 nlUij Link__StyledStandardLink-e9c1rj-0 eZMnyW"][1]//span')

    def __init__(self, web_element):
        super().__init__(*tuple(web_element.__dict__.values()))

    @property
    def name(self):
        return self.find_element(*self.by_name).text

    @property
    def url(self):
        return self.find_element(*self.by_url).get_attribute('href')


class CapterraComPage(BasePage):

    by_row = (By.CLASS_NAME, 'DesktopProductCard__ProductCardInfo-v49nag-4.jupdha')

    def __init__(self, executable_path):
        super().__init__(executable_path)
        self.driver.get('https://www.capterra.com/architecture-software/')
        rows = self.driver.find_elements(*self.by_row)
        self.rows = [CapterraComPageRow(row) for row in rows]

    def get_rows(self):
        yield from self.rows

    def tear_down(self):
        self.driver.quit()
