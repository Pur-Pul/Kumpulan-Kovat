class CitationService:
    def __init__(self, citation_repository):
        self._citation_repository = citation_repository

    def create_citation(self, citation_name, title, year, author):
        self._citation_repository.insert_citation(
            citation_name, title, year, author)

    def get_citation(self, id):
        return self._citation_repository.get_citation(id)

    def get_citations(self):
        return self._citation_repository.get_citations()

    def citation_search(self):
        return self._citation_repository.citation_search()
