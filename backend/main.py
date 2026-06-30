import asyncio

from app.cli.controller import (
    cli_controller,
)


if __name__ == "__main__":

    asyncio.run(

        cli_controller.start()

    )