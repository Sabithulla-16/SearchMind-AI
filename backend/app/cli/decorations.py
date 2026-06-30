import shutil


class Decorations:

    def __init__(self):

        self.width = shutil.get_terminal_size(
            fallback=(100, 30)
        ).columns

    def line(
        self,
        character: str = "=",
    ):

        print(character * self.width)

    def separator(self):

        self.line("-")

    def blank(self):

        print()

    def title(
        self,
        text: str,
    ):

        self.line("=")
        print(text.center(self.width))
        self.line("=")

    def subtitle(
        self,
        text: str,
    ):

        self.blank()
        print(text.center(self.width))
        self.separator()

    def section(
        self,
        title: str,
    ):

        self.blank()
        print(title)
        self.separator()

    def success(
        self,
        message: str,
    ):

        print(f"[SUCCESS] {message}")

    def warning(
        self,
        message: str,
    ):

        print(f"[WARNING] {message}")

    def error(
        self,
        message: str,
    ):

        print(f"[ERROR] {message}")

    def info(
        self,
        message: str,
    ):

        print(f"[INFO] {message}")

    def banner(self):

        self.line("=")

        print(
            "SEARCHMIND AI".center(
                self.width
            )
        )

        print(
            "Intelligent Multi-Source Search Engine".center(
                self.width
            )
        )

        self.line("=")

    def goodbye(self):

        self.blank()

        self.line("=")

        print(
            "Thank you for using SearchMind AI".center(
                self.width
            )
        )

        self.line("=")


decorations = Decorations()