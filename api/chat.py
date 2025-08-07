import abc 

from .base_process import BaseProcess, MessageTypeError
from .message import Message, Tags


class IChat(abc.ABC):

    @abc.abstractmethod
    def send(self, content: str): ...

    @abc.abstractmethod
    def report_error(self, content: str): ...


class ChatProcess(BaseProcess):

    def __init__(self, chat: IChat, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat = chat

    def on_message(self, message: Message):
        match message.tag:
            case Tags.MESSAGE:
                self.chat.send(message.content)
            
            case Tags.ERROR:
                self.chat.report_error(message.content)

            case Tags.EXTERNAL_ERROR:
                self.output.put(message)
                self.close()

            case Tags.EXTENRAL_REQUEST:
                self.output.put(Message(Tags.MESSAGE, message.content))

            case _:
                raise MessageTypeError(message.tag, type(self))        
