from pathlib import Path

from git import Repo

from app.sources.github.config import (
    TEMP_REPOSITORY_DIR,
)


class GitHubCloner:

    def clone(
        self,
        repository_url: str,
    ):

        repository_name = (
            repository_url.rstrip("/")
            .split("/")[-1]
        )

        destination = (
            TEMP_REPOSITORY_DIR
            / repository_name
        )

        TEMP_REPOSITORY_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        # -------------------------
        # Reuse existing clone
        # -------------------------

        if destination.exists():

            return destination

        # -------------------------
        # Clone repository
        # -------------------------

        Repo.clone_from(

            repository_url,

            destination,

        )

        return destination


github_cloner = GitHubCloner()