# Python <3
import csv
import time
import traceback


class BaseScraper:
    """Base scraper class to inherit in page scrapers."""

    count = 0
    begin = 0
    end = 0

    def __init__(self, page, headers):
        self.begin = time.time()
        self.page = page
        self.headers = headers
        try:
            self.begin_scrap()
        except Exception:
            self.finish()
            traceback.print_exc()

    def begin_scrap(self):
        with open('result.csv', mode='w') as result:
            result = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result.writerow([header.capitalize()+':' for header in self.headers])
            rows = self.page.get_rows()
            while True:
                try:
                    row = next(rows)
                    self.count += 1
                    print(f'Writing line: {self.count}')
                    result.writerow([getattr(row, header) for header in self.headers])
                except StopIteration:
                    break
            self.finish()

    def finish(self):
        self.page.tear_down()
        self.end = time.time()
        print('_________________________')
        print(f'Scrap finished with {self.count} lines in {(self.end - self.begin) % 60} seconds. See you next time! :)')
