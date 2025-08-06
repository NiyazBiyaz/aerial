from abc import ABC, abstractmethod


class IChatProvider(ABC):

    @abstractmethod
    def push_message(text: str): ...

    @abstractmethod
    def report_error(code: int, message: str): ...
