from app.sources.base import BaseSource

from app.sources.github.clone import (
    github_cloner,
)

from app.sources.filesystem.source import (
    filesystem_source,
)

class GitHubSource(BaseSource):

    name = "github"

    async def retrieve(
        self,
        repository_url: str,
    ):

        folder = github_cloner.clone(
            repository_url
        )

        result = await filesystem_source.retrieve(
            folder=str(folder),
        )

        result.source = "github"

        return result


github_source = GitHubSource()