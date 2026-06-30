import re

from pathlib import Path

from datetime import datetime

from app.cli.decorations import decorations


OUTPUT_DIRECTORY = Path("outputs")


class SaveManager:

    def __init__(self):

        OUTPUT_DIRECTORY.mkdir(
            exist_ok=True
        )

    def clean_markdown(
        self,
        text: str,
    ):

        text = re.sub(
            r"\*\*(.*?)\*\*",
            r"\1",
            text,
        )

        text = re.sub(
            r"__(.*?)__",
            r"\1",
            text,
        )

        text = re.sub(
            r"`(.*?)`",
            r"\1",
            text,
        )

        text = re.sub(
            r"#+ ",
            "",
            text,
        )

        text = re.sub(
            r"\[(.*?)\]\((.*?)\)",
            r"\1",
            text,
        )

        return text

    def ask(
        self,
        result,
    ):

        print()

        choice = input(
            "Save response as TXT? (y/n): "
        ).strip().lower()

        if choice != "y":

            return

        filename = input(
            "Filename (leave blank for auto): "
        ).strip()

        if not filename:

            filename = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

        filename += ".txt"

        path = OUTPUT_DIRECTORY / filename

        answer = self.clean_markdown(
            result.answer
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write("SearchMind AI\n")
            file.write("=" * 60)
            file.write("\n\n")

            file.write("Answer\n")
            file.write("-" * 20)
            file.write("\n")
            file.write(answer)
            file.write("\n\n")

            file.write("Sources\n")
            file.write("-" * 20)
            file.write("\n")

            for index, source in enumerate(
                result.sources,
                start=1,
            ):

                file.write(
                    f"{index}. {source.title}\n"
                )

                file.write(
                    f"{source.url}\n\n"
                )

        decorations.success(
            f"Saved to {path}"
        )


save_manager = SaveManager()