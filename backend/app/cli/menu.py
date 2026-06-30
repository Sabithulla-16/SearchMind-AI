from app.cli.decorations import decorations


class Menu:

    OPTIONS = {

        "1": "Web Search",

        "2": "PDF Document",

        "3": "Filesystem Folder",

        "4": "GitHub Repository",

        "5": "Multi Source",

        "0": "Exit",

    }

    def show(self):

        while True:

            decorations.banner()

            decorations.section("Main Menu")

            for key, value in self.OPTIONS.items():

                print(f"[{key}] {value}")

            print()

            choice = input(
                "Select an option: "
            ).strip()

            if choice in self.OPTIONS:

                return choice

            decorations.blank()

            decorations.error(
                "Invalid option. Please try again."
            )

            input(
                "\nPress Enter to continue..."
            )


menu = Menu()