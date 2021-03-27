# Selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Project
from pages.base_page import BasePage


class SignalFxPageRow(WebElement):

    url_replacement = ('file:///', 'https://signal.nfx.com/')

    by_name = (By.XPATH, './/strong[contains(@class, "sn-investor-name")]')
    by_link = (By.XPATH, './/a[contains(@href, "investors") and contains(@style, "white")]')
    by_company = (By.XPATH, './/td[1]//div[@class="sn-investor-name-wrapper"]/a')
    by_role = (By.XPATH, './/td[1]//div[@class="sn-investor-name-wrapper"]/span')
    by_sweet_spot = (By.XPATH, './/td[2]//div[@class="flex-column"]//div[1]')
    by_range = (By.XPATH, './/td[2]//div[@class="flex-column"]//div[2]')
    by_investments = (By.XPATH, './/td[3]//span//a')
    by_categories = (By.XPATH, './/td[4]//span//a')

    def __init__(self, web_element):
        super().__init__(*tuple(web_element.__dict__.values()))

    @property
    def name(self):
        return self.find_element(*self.by_name).text

    @property
    def link(self):
        href = self.find_element(*self.by_link).get_attribute('href')
        return href.replace(*self.url_replacement)

    @property
    def company(self):
        try:
            return self.find_element(*self.by_company)
        except NoSuchElementException:
            return ''

    @property
    def company_text(self):
        try:
            return self.company.text
        except AttributeError:
            return ''

    @property
    def company_link(self):
        try:
            href = self.company.get_attribute('href')
            return href.replace(*self.url_replacement)
        except AttributeError:
            return ''

    @property
    def role(self):
        try:
            return self.find_element(*self.by_role).text
        except NoSuchElementException:
            return ''

    @property
    def sweet_spot(self):
        return self.find_element(*self.by_sweet_spot).text

    @property
    def range(self):
        return self.find_element(*self.by_range).text

    @property
    def investments(self):
        investments = self.find_elements(*self.by_investments)
        ret = ''
        for inv in investments:
            if ret:
                ret = ret + ', '
            ret = ret + inv.text
        return ret

    @property
    def categories(self):
        categories = self.find_elements(*self.by_categories)
        ret = ''
        for inv in categories:
            if ret:
                ret = ret + ', '
            ret = ret + inv.text
        return ret


class SignalFxPage(BasePage):

    by_row = (By.XPATH, './/table//tbody//tr')
    page_url = 'file:///home/gonza/PycharmProjects/scrappy/html/signal.html'
    page_row_class = SignalFxPageRow

    def __init__(self, executable_path):
        super().__init__(executable_path, self.page_url, self.by_row, self.page_row_class)
