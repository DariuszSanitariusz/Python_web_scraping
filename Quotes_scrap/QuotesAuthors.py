class QuotesAuthors:
    def __init__(self):
        self.set_of_authors = set()

    def authors_on_page(self, soup):
        for author in soup.select('.author'):
            self.set_of_authors.add(author.text)

    def new_page(self):
        self.set_of_authors.clear()

    def author_bio(self, soup):
        bio = soup.select('.author-description')
        return bio.text
