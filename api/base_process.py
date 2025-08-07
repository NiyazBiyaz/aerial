import abc
import multiprocessing as mpc
from typing import Any

import api.message as message


class MessageTypeError(Exception):

    def __init__(self, value: Any, process: "BaseProcess"):
        super().__init__(f"Type {value} unexpected for {process}")


class BaseProcess(mpc.Process):

    @abc.abstractmethod
    def on_message(self, message: message.Message): ...


    def __init__(self, input_queue: mpc.Queue, output_queue: mpc.Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input = input_queue
        self._output = output_queue


    def run(self):
        while True:
            msg = self.input.get()
            self.on_message(msg)
