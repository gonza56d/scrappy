"""Implementation of AngelCoPage"""

# Python <3
import csv, time, traceback

# Project
from pages import AngelCoPage


class AngelCoScrapper:

    page_class = AngelCoPage
    count = 0
    begin = 0
    end = 0

    def __init__(self, executable_path):
        self.begin = time.time()
        self.page = self.page_class(executable_path)
        try:
            self.begin_scrap()
        except Exception:
            self.finish()
            traceback.print_exc()

    def begin_scrap(self):
        with open('resut.csv', mode='w') as result:
            result = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result.writerow(['Names:', 'Description:', 'Location', 'Area', 'Investments:', 'Followers:'])
            rows = self.page.get_rows()
            while True:
                try:
                    row = next(rows)
                    self.count += 1
                    print(f'Writing line: {self.count}')
                    result.writerow([row.name, row.description, row.location, row.area, row.investments, row.followers])
                except StopIteration:
                    break
            self.finish()

    def finish(self):
        self.page.tear_down()
        self.end = time.time()
        print('_________________________')
        print(f'Scrap finished with {self.count} lines in {(self.end - self.begin) % 60} seconds. See you next time! :)')
