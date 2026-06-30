from app.retriever.models import RetrievalStatistics


class StatisticsTracker:

    def __init__(self):
        self.reset()

    def reset(self):
        self.stats = RetrievalStatistics()

    def attempted(self):
        self.stats.attempted += 1

    def success(self):
        self.stats.successful += 1

    def failed(self):
        self.stats.failed += 1

    def skipped(self):
        self.stats.skipped += 1

    def summary(self):
        return self.stats


statistics_tracker = StatisticsTracker()