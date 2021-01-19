from selenium import webdriver


class BasePage:

    rows = None

    def __init__(self, executable_path, page_url, by_row, page_row_class):
        self.driver = webdriver.Chrome(executable_path=executable_path)
        self.driver.maximize_window()
        self.driver.get(page_url)
        rows = self.driver.find_elements(*by_row)
        self.rows = [page_row_class(row, self.driver) for row in rows]

    def get_rows(self):
        yield from self.rows

    def tear_down(self):
        self.driver.quit()
