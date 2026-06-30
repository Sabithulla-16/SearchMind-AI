import time


class Timer:

    def __init__(self):

        self.started = None

    def start(self):

        self.started = time.perf_counter()

    def stop(self):

        if self.started is None:
            return 0

        return (
            time.perf_counter()
            - self.started
        ) * 1000