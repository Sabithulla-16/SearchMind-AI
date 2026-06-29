from abc import ABC, abstractmethod


class BaseFetcher(ABC):

    @abstractmethod
    async def fetch(self, source: str) -> str:
        pass