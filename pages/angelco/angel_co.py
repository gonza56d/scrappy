"""https://angel.co/fintech-2/investors"""

# Selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Project
from pages.base_page import BasePage


class AngelCoPageRow(WebElement):

    by_name = (By.XPATH, './/div[@class="name"]//a[@class="profile-link"]')
    by_description = (By.CLASS_NAME, 'blurb')
    by_tags = (By.XPATH, './/div[@class="tags"]//a')
    by_first_tag = (By.XPATH, './/div[@class="tags"]//a[1]')
    by_second_tag = (By.XPATH, './/div[@class="tags"]//a[2]')
    by_investments = (By.XPATH, './/div[@class="column investments"]//div[@class="value"]')
    by_followers = (By.XPATH, './/div[@class="column followers"]//div[@class="value"]')

    def __init__(self, web_element):
        super().__init__(*tuple(web_element.__dict__.values()))

    @property
    def name(self):
        return self.find_element(*self.by_name).text

    @property
    def description(self):
        try:
            return self.find_element(*self.by_description).text
        except NoSuchElementException:
            return ''

    @property
    def tags(self):
        return self.find_elements(*self.by_tags)

    @property
    def location(self):
        if len(self.tags) > 1:
            return self.find_element(*self.by_first_tag).text
        elif len(self.tags) == 1:
            return ''

    @property
    def area(self):
        if len(self.tags) > 1:
            return self.find_element(*self.by_second_tag).text
        elif len(self.tags) == 1:
            return self.find_element(*self.by_first_tag).text

    @property
    def investments(self):
        return self.find_element(*self.by_investments).text

    @property
    def followers(self):
        return self.find_element(*self.by_followers).text


class AngelCoPage(BasePage):

    by_row = (By.CLASS_NAME, 'base.item')

    def __init__(self, executable_path):
        super().__init__(executable_path)
        self.driver.get('file:///home/gonza/PycharmProjects/scrappy/html/angel_co.html')
        rows = self.driver.find_elements(*self.by_row)
        self.rows = [AngelCoPageRow(row) for row in rows]

    def get_rows(self):
        yield from self.rows
