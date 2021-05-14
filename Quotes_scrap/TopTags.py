class TopTags:
    def __init__(self):
        self.list_of_trend_tags = []

    def top_tags(self, soup):
        for n in range(0, 10):
            self.list_of_trend_tags.append((soup.select('.tag-item')[n].getText()).rstrip())
