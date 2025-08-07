import abc
import multiprocessing as mpc
import queue
from typing import Any

import api.message as message


class MessageTypeError(Exception):

    def __init__(self, value: Any, process: "BaseProcess"):
        super().__init__(f"Tag {value} unexpected for {process}")


class BaseProcess(mpc.Process):

    @abc.abstractmethod
    def on_message(self, message: message.Message): ...


    def __init__(self, input_queue: mpc.Queue, output_queue: mpc.Queue, stop_event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input = input_queue
        self.output = output_queue
        self.stop_event = stop_event


    def run(self):
        try:
            while not self.stop_event.is_set():
                    try:
                        msg = self.input.get(timeout=1)
                        self.on_message(msg)
                    except queue.Empty:
                        continue
        finally:
            self.close()


    def close(self):
        self.stop_event.set()
        super().close()
