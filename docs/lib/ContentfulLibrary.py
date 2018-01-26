from context import content
from content.guides import search_guides


class ContentfulLibrary:

    def __init__(self):
        pass

    def search_for_guides(self, query):
        search_guides(query)
