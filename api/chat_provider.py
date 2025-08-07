from abc import ABC, abstractmethod


class IChatProvider(ABC):

    @abstractmethod
    def push_message(self, text: str): ...

    @abstractmethod
    def report_error(self, code: int, message: str): ...
