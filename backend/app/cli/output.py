from app.cli.decorations import decorations


class Output:

    def answer(
        self,
        result,
    ):

        decorations.title(
            "FINAL ANSWER"
        )

        print(result.answer)

        decorations.blank()

    def sources(
        self,
        result,
    ):

        decorations.section(
            "Sources"
        )

        for index, source in enumerate(
            result.sources,
            start=1,
        ):

            print(f"[{index}] {source.title}")
            print(source.url)
            print()

    def statistics(
        self,
        metrics: dict,
    ):

        decorations.section(
            "Statistics"
        )

        for key, value in metrics.items():

            print(f"{key:<25} : {value}")

    def pipeline_finished(self):

        decorations.success(
            "Pipeline completed successfully."
        )

    def pipeline_failed(
        self,
        message: str,
    ):

        decorations.error(
            message
        )


output = Output()