from pathlib import Path

from app.cli.decorations import decorations

from app.sources.models import SourceRequest


class InputHandler:

    def web(self):

        decorations.section("Web Search")

        query = input(
            "Search Query : "
        ).strip()

        return query

    def pdf(self):

        decorations.section("PDF Document")

        path = Path(

            input(
                "PDF Path     : "
            )
            .strip()
            .replace("\u202a", "")

        ).expanduser()

        query = input(
            "Question : "
        ).strip()

        return str(path), query

    def filesystem(self):

        decorations.section(
            "Filesystem Folder"
        )

        folder = Path(

            input(
                "Folder Path  : "
            )
            .strip()
            .replace("\u202a", "")

        ).expanduser()

        query = input(
            "Question : "
        ).strip()

        return str(folder), query

    def github(self):

        decorations.section(
            "GitHub Repository"
        )

        repository = input(

            "Repository URL : "

        ).strip()

        query = input(
            "Question : "
        ).strip()

        return repository, query

    def multi_source(self):

        decorations.section(
            "Multi Source"
        )

        query = input(
            "Search Query      : "
        ).strip()

        pdf = input(
            "PDF Path          : "
        ).strip()

        folder = input(
            "Folder Path       : "
        ).strip()

        github = input(
            "Repository URL    : "
        ).strip()

        pdf_paths = []

        folders = []

        github_repositories = []

        if pdf:

            pdf_paths.append(
                pdf.replace("\u202a", "")
            )

        if folder:

            folders.append(
                folder.replace("\u202a", "")
            )

        if github:

            github_repositories.append(
                github
            )

        return (

            query,

            pdf_paths,

            folders,

            github_repositories,

        )


input_handler = InputHandler()