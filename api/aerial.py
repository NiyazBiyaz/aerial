from abc import ABC, abstractmethod


class IAerial(ABC):

    @abstractmethod
    def pull_message(self, text: str): ...

    @abstractmethod
    def done(self): ...
