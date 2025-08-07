import abc

from api.base_process import BaseProcess, MessageTypeError
from api.message import Tags, Message


class IAerial(abc.ABC):

    @abc.abstractmethod
    def create_response(self, question: str) -> str: ...

    @abc.abstractmethod
    def close(self) -> None: ...


class AerialProcess(BaseProcess):

    def __init__(self, aerial: IAerial, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._aerial = aerial


    def on_message(self, message: Message):
        match message.tag:

            case Tags.MESSAGE:
                try:
                    response = self._aerial.create_response(message.content)
                    self.output.put(Message(Tags.MESSAGE, response))
                except Exception as e:
                    self.output.put(Message(Tags.ERROR, str(e)))
                    self.close()

            case Tags.DONE | Tags.EXTERNAL_ERROR:
                self.close()

            case _:
                raise MessageTypeError(message.tag, type(self))


    def close(self):
        self._aerial.close()
        super().close()
