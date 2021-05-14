from QuotesAuthors import QuotesAuthors
from Quotes import Quotes
from TopTags import TopTags
from Page import Page
from CreateCsv import CreateCsv

page = Page()
page_q_authors = QuotesAuthors()
page_quotes = Quotes()

page_to_scrap = Page()
page_to_scrap.page_soup()
page_to_scrap.check_page()

current_top_tags = TopTags()
current_top_tags.top_tags(page_to_scrap.soup)

while not page_to_scrap.check_empty:
    page_q_authors.authors_on_page(page_to_scrap.soup)
    page_quotes.quotes_on_page(page_to_scrap.soup)

    page_to_scrap.authors_add(page_q_authors.set_of_authors)
    page_to_scrap.quotes_add(page_quotes.list_of_quotes)

    page_to_scrap.page_number += 1
    page_to_scrap.page_soup()

    page_q_authors.clear_authors()
    page_quotes.clear_quotes()

    page_to_scrap.check_page()


file = CreateCsv('quotes.csv')
file.open_file()
file.first_line()

for author_name in page_to_scrap.all_authors:
    row = []
    page_to_scrap.bio_soup(author_name)
    bio_text = page_q_authors.author_bio(page_to_scrap.soup)
    page_to_scrap.bio_add(author_name, bio_text)

    row.extend([author_name, page_to_scrap.all_bios[author_name], page_to_scrap.all_quotes[author_name]])

    file.add_line(row)

file.close_file()





