from dataclasses import dataclass
import enum


@dataclass
class Message:
    type: "Types"
    content: str


@enum.unique
class Types(enum.Enum):
    MESSAGE  = 1
    DONE  = 2
    ERROR = 3
    EXTENRAL_REQUEST = 4
