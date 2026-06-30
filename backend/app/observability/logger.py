from app.observability.config import *


class PipelineLogger:

    def print_metrics(
        self,
        metrics,
    ):

        if not SHOW_STAGE_TIMINGS:
            return

        print("\nPipeline Timings")
        print("--------------------------")

        total = 0

        for stage in metrics.stages.values():

            total += stage.duration_ms

            print(
                f"{stage.name:<20}"
                f"{stage.duration_ms:.2f} ms"
            )

        print("--------------------------")
        print(
            f"{'Total':<20}"
            f"{total:.2f} ms"
        )

    def print_counters(
        self,
        metrics,
    ):

        if not SHOW_METRICS:
            return

        print("\nPipeline Metrics")
        print("--------------------------")

        for key, value in metrics.counters.items():

            print(
                f"{key:<25}{value}"
            )

    def print_timeline(
        self,
        events,
    ):

        if not SHOW_TIMELINE:
            return

        print("\nPipeline Timeline")
        print("--------------------------")

        for time, event in events:

            print(
                f"[{time}] {event}"
            )


pipeline_logger = PipelineLogger()