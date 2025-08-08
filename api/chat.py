import abc 
import asyncio
import multiprocessing as mpc
from typing import Union

from .message import Message, Tags, MessageTypeError


class BaseChat(abc.ABC):

    def __init__(self, to_me_queue: mpc.Queue, from_me_queue: mpc.Queue):
        """
        Args:
            to_me_queue (Queue): messages **TO** this process
            from_me_queue (Queue): messages **FROM** this process
        """
        self.to_me = to_me_queue
        self.from_me = from_me_queue


    @abc.abstractmethod
    async def report_error(self, response: Message) -> None:
        """
        Method for notify User about internal error. 
        Must be overrided from chat-provided environment

        Args:
            response (Message): Information about error 
        """


    async def create_answer(self, question: str) -> Union[str | None]:
        await asyncio.to_thread(self.from_me.put, Message(Tags.MESSAGE, question))
        response: Message = await asyncio.to_thread(self.to_me.get)

        match response.tag:
            case Tags.MESSAGE:
                return response.content
            
            case Tags.ERROR:
                await self.report_error(response)
                return None

            case _ as tag:
                self.close_aerial(Tags.ERROR)
                raise MessageTypeError(tag)


    async def close_aerial(self, tag: Tags):
        if tag in [Tags.ERROR, Tags.DONE]:
            await asyncio.to_thread(self.from_me.put, Message(tag, ""))
        else:
            await asyncio.to_thread(self.from_me.put, Message(Tags.ERROR, ""))
            raise MessageTypeError(tag)
