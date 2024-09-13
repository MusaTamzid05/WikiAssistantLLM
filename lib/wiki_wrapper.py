import wikipediaapi

class WikiWrapper:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia("Summary Project (musa@email.com)", "en")

    def get_summary(self, name):
        page = self.wiki.page(name)

        if page.exists() == False:
            return None

        return page.summary





if __name__ == "__main__":
    wiki_wrapper = WikiWrapper()
    summary = wiki_wrapper.get_summary(name="Apple")
    print(summary)


