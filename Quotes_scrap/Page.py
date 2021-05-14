import requests
import bs4
import unidecode

class Page:
    def __init__(self):
        self.page_url = 'http://quotes.toscrape.com/page/{}/'
        self.author_bio_url = 'http://quotes.toscrape.com/author/{}/'
        self.soup = 0
        self.page_number = 1
        self.all_authors = set()
        self.all_bios = {}
        self.all_quotes = {}
        self.check_empty = False

    def page_soup(self):
        res = requests.get(self.page_url.format(self.page_number))
        self.soup = bs4.BeautifulSoup(res.text, 'lxml')

    def check_page(self):
        if len(self.soup.select('.quote')):
            self.check_empty = False
        else:
            self.check_empty = True

    def authors_add(self, authors):
        self.all_authors.update(authors)

    def bio_soup(self, author):
        author = unidecode.unidecode(author)
        author = list(author)
        for n in range(len(author)):
            try:
                if author[n+1].isupper():
                    author[n] = '-'
            except IndexError:
                pass
        author = ''.join(author).replace('.', '')
        res = requests.get(self.author_bio_url.format(author))
        self.soup = bs4.BeautifulSoup(res.text, 'lxml')

    def bio_add(self, author, bio):
        bio = bio.replace('\r', '')
        bio = bio.replace('\n', '')
        self.all_bios[author] = bio[8:-9]

    def quotes_add(self, quotes):
        for author, quote in quotes:
            while True:
                try:
                    self.all_quotes[author].append(quote[1:-1])
                except KeyError:
                    self.all_quotes[author] = []
                else:
                    break
