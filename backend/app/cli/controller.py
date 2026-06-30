from app.cli.decorations import decorations
from app.cli.menu import menu
from app.cli.input_handler import input_handler
from app.cli.output import output
from app.cli.save import save_manager

from app.pipeline.search_pipeline import search_pipeline

from app.pipeline.filesystem_pipeline import (
    filesystem_pipeline,
)

from app.pipeline.github_pipeline import (
    github_pipeline,
)

from app.pipeline.pdf_pipeline import (
    pdf_pipeline,
)

from app.pipeline.multisource_pipeline import (
    multisource_pipeline,
)

class CLIController:

    async def start(self):

        while True:

            choice = menu.show()

            if choice == "0":

                decorations.goodbye()
                break

            try:

                await self.handle_choice(
                    choice
                )

            except Exception as error:

                decorations.error(
                    str(error)
                )

            print()

            input(
                "Press Enter to continue..."
            )

    async def handle_choice(
        self,
        choice: str,
    ):

        # -------------------------
        # WEB
        # -------------------------

        if choice == "1":

            query = input_handler.web()

            result = await search_pipeline.run(
                query
            )

            generation = result["generation"]

            output.answer(generation)

            output.sources(generation)

            save_manager.ask(generation)

            return

        # -------------------------
        # PDF
        # -------------------------

        if choice == "2":

            pdf_path, query = input_handler.pdf()

            result = await pdf_pipeline.run(
                pdf_path=pdf_path,
                query=query,
            )

            generation = result["generation"]

            output.answer(generation)
            output.sources(generation)

            save_manager.ask(generation)

            return

        # -------------------------
        # FILESYSTEM
        # -------------------------

        if choice == "3":

            folder, query = input_handler.filesystem()

            result = await filesystem_pipeline.run(
                folder=folder,
                query=query,
            )

            generation = result["generation"]

            output.answer(generation)
            output.sources(generation)

            save_manager.ask(generation)

            return

        # -------------------------
        # GITHUB
        # -------------------------

        if choice == "4":

            repository, query = input_handler.github()

            result = await github_pipeline.run(
                repository=repository,
                query=query,
            )

            generation = result["generation"]

            output.answer(generation)
            output.sources(generation)

            save_manager.ask(generation)

            return

        # -------------------------
        # MULTI SOURCE
        # -------------------------

        if choice == "5":

            (
                query,
                pdf_paths,
                folders,
                github_repositories,
            ) = input_handler.multi_source()

            result = await multisource_pipeline.run(

                query=query,

                pdf_paths=pdf_paths,

                folders=folders,

                github_repositories=github_repositories,

            )

            generation = result["generation"]

            output.answer(generation)

            output.sources(generation)

            save_manager.ask(generation)

            return


cli_controller = CLIController()