import time


class PipelineTracer:

    def __init__(self):

        self.reset()

    def reset(self):

        self.events = []

    def trace(
        self,
        event: str,
    ):

        self.events.append(

            (

                time.strftime("%H:%M:%S"),

                event,

            )

        )

    def summary(self):

        return self.events


pipeline_tracer = PipelineTracer()