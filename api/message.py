from dataclasses import dataclass
import enum
from typing import Any


@dataclass
class Message:
    tag: "Tags"
    content: str


@enum.unique
class Tags(enum.Enum):
    MESSAGE  = 1
    DONE  = 2
    ERROR = 3


class MessageTypeError(Exception):

    def __init__(self, value: Any):
        super().__init__(f"Unexpected tag value: {value}")
