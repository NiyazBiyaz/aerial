from abc import ABC, abstractmethod


class IAerial(ABC):

    @abstractmethod
    def pull_message(text: str): ...

    @abstractmethod
    def done(): ...
