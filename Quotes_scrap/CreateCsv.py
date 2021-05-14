import csv


class CreateCsv:
    def __init__(self, file_name):
        self.file_name = file_name
        self.quotes_csv = 0

    def open_file(self):
        self.quotes_csv = open(self.file_name, mode='w', encoding='UTF-8', newline='')

    def first_line(self):
        quotes_writer = csv.writer(self.quotes_csv, delimiter=',')
        quotes_writer.writerow(['author', 'biography', 'quotes'])

    def add_line(self, row):
        quotes_writer = csv.writer(self.quotes_csv, delimiter=',')
        quotes_writer.writerow(row)

    def close_file(self):
        self.quotes_csv.close()
