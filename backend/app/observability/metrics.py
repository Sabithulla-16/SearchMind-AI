from app.observability.models import (
    PipelineMetrics,
    StageMetric,
)


class MetricsCollector:

    def __init__(self):

        self.reset()

    def reset(self):

        self.metrics = PipelineMetrics()

    def record_stage(
        self,
        stage: str,
        duration: float,
    ):

        self.metrics.stages[stage] = StageMetric(

            name=stage,

            duration_ms=duration,

        )

    def increment(
        self,
        key: str,
        value: int = 1,
    ):

        self.metrics.counters[key] = (

            self.metrics.counters.get(
                key,
                0,
            )

            + value

        )

    def set_counter(
        self,
        key: str,
        value: int,
    ):

        self.metrics.counters[key] = value

    def summary(self):

        return self.metrics


metrics_collector = MetricsCollector()