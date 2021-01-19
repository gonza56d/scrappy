"""https://www.capterra.com/architecture-software/"""

# Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Project
from pages import BasePage


class CapterraComPageRow(WebElement):

    by_name = (By.XPATH, './/a[@class="ProductHeaderSection__ProductHeaderLink-sc-55o1a3-1 nlUij Link__StyledStandardLink-e9c1rj-0 eZMnyW"][1]//span')
    by_url = (By.XPATH, './/a[@class="ProductHeaderSection__ProductHeaderLink-sc-55o1a3-1 nlUij Link__StyledStandardLink-e9c1rj-0 eZMnyW"][1]')
    by_description = (By.XPATH, './/div[@class="DesktopProductCard__ProductCardDescription-v49nag-5 gZtRlf"]')
    by_by = (By.XPATH, './/h3[@class="VendorNameContainer__VendorHeading-sc-1ns38vc-0 klpzVA Heading-y0oiys-2 kdQRDY"][1]//span')

    def __init__(self, web_element):
        super().__init__(*tuple(web_element.__dict__.values()))

    @property
    def name(self):
        return self.find_element(*self.by_name).text

    @property
    def url(self):
        return self.find_element(*self.by_url).get_attribute('href')

    @property
    def description(self):
        return self.find_element(*self.by_description).text

    @property
    def by(self):
        return self.find_element(*self.by_by).text


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
