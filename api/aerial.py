import abc
import multiprocessing as mpc
from typing import Any
import queue

from api.message import Tags, Message, MessageTypeError


class IAerial(abc.ABC):

    @abc.abstractmethod
    def create_response(self, question: str) -> str: ...

    @abc.abstractmethod
    def close(self) -> None: ...


class AerialProcess(mpc.Process):

    def __init__(self, to_me_queue: mpc.Queue, from_me_queue: mpc.Queue, aerial: IAerial, timeout: float = 5.0):
        """
        Args:
            to_me_queue (Queue): messages to this process
            from_me_queue (Queue): messages from this process
            aerial (IAerial): Aerial implementaion
            timeout (float, optional): Log frequency with no working. Defaults to 5.0.
        """
        self._to_me = to_me_queue
        self._from_me = from_me_queue
        self._aerial = aerial
        self._timeout = timeout
        super().__init__()


    def on_message(self, message: Message):
        match message.tag:
            case Tags.MESSAGE:
                try:
                    response = self._aerial.create_response(message.content)
                    self._from_me.put(Message(Tags.MESSAGE, response))
                except Exception as e:
                    raise InternalAerialError() from e

            case Tags.DONE | Tags.ERROR:
                self.shutdown()

            case _:
                raise MessageTypeError(message.tag)


    def run(self):
        try:
            while True:
                try:
                    msg = self._to_me.get(timeout=self._timeout)
                    self.on_message(msg)
                except queue.Empty:
                    print("make a log here, pls")
        except Exception as e:
            self.shutdown(e)
            raise


    def shutdown(self, excpeption: Exception | None = None):
        if excpeption:
            self._from_me.put(Message(Tags.ERROR, str(excpeption)))
        self._aerial.close()
        super().close()


class InternalAerialError(Exception):

    def __init__(self):
        super().__init__("Aerial internal logic error.")
