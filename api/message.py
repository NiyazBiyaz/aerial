from dataclasses import dataclass
import enum


@dataclass
class Message:
    tag: "Tags"
    content: str


@enum.unique
class Tags(enum.Enum):
    MESSAGE  = 1
    DONE  = 2
    ERROR = 3
    EXTERNAL_REQUEST = 4
    EXTERNAL_ERROR = 5
