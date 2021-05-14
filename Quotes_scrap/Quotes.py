class Quotes:
    def __init__(self):
        self.list_of_quotes = []

    def quotes_on_page(self, soup):
        quotes_list = []
        n = 0
        for quote in soup.select('.text'):
            quotes_list.append(quote.text)
        for author in soup.select('.author'):
            self.list_of_quotes.append((author.text, quotes_list[n]))
            n += 1

    def clear_quotes(self):
        self.list_of_quotes.clear()
