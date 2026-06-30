from app.sources.web.source import web_source
from app.sources.pdf.source import pdf_source
from app.sources.filesystem.source import filesystem_source
from app.sources.github.source import github_source

class SourceRegistry:

    def __init__(self):

        self.sources = {}

    def register(
        self,
        source,
    ):

        self.sources[source.name] = source

    def get(
        self,
        name: str,
    ):

        return self.sources.get(name)

    def all(self):

        return list(self.sources.values())

    def available_sources(self):

        return list(self.sources.keys())


source_registry = SourceRegistry()

# ---------------------------------------
# Register all available sources
# ---------------------------------------

source_registry.register(
    web_source
)

source_registry.register(
    pdf_source
)

source_registry.register(
    filesystem_source
)

source_registry.register(
    github_source
)