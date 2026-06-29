import re


class Cleaner:

    def clean(
        self,
        text: str,
    ):

        text = re.sub(
            r"\n+",
            "\n",
            text,
        )

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        return text.strip()


cleaner = Cleaner()