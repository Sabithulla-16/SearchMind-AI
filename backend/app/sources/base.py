from abc import ABC, abstractmethod


class BaseSource(ABC):

    name: str

    @abstractmethod
    async def retrieve(
        self,
        *args,
        **kwargs,
    ):
        pass