from app.observability.timer import Timer

from app.observability.metrics import (
    metrics_collector,
)

from app.observability.tracer import (
    pipeline_tracer,
)

from app.observability.logger import (
    pipeline_logger,
)


class ObservabilityService:

    def __init__(self):

        self.timers = {}

    def reset(self):

        self.timers.clear()

        metrics_collector.reset()

        pipeline_tracer.reset()

    def start(
        self,
        stage: str,
    ):

        timer = Timer()

        timer.start()

        self.timers[stage] = timer

        pipeline_tracer.trace(
            f"{stage} Started"
        )

    def stop(
        self,
        stage: str,
    ):

        timer = self.timers.get(stage)

        if timer is None:
            return

        duration = timer.stop()

        metrics_collector.record_stage(
            stage,
            duration,
        )

        pipeline_tracer.trace(
            f"{stage} Finished"
        )

    def counter(
        self,
        key: str,
        value: int,
    ):

        metrics_collector.set_counter(
            key,
            value,
        )

    def summary(self):

        metrics = metrics_collector.summary()

        pipeline_logger.print_metrics(
            metrics
        )

        pipeline_logger.print_counters(
            metrics
        )

        pipeline_logger.print_timeline(
            pipeline_tracer.summary()
        )

    def metrics(self):

        return metrics_collector.summary()

    def timeline(self):

        return pipeline_tracer.summary()


observability_service = ObservabilityService()