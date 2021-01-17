from selenium import webdriver


class BasePage:

    def __init__(self, executable_path):
        self.driver = webdriver.Chrome(executable_path=executable_path)
        self.driver.maximize_window()
