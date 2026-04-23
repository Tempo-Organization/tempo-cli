from enum import Enum
from typing import Type, TypeVar


class RichColorSystem(Enum):
    """
    Enum for which Rich Color System to be used
    """
    AUTO = 'auto'
    STANDARD = 'standard'
    COLOR_256 = '256'
    TRUECOLOR = 'truecolor'
    WINDOWS = 'windows'
    NONE = 'none'


E = TypeVar("E", bound=Enum)

def get_enum_from_val[E: Enum](enum_cls: type[E], value: object) -> E:
    for entry in enum_cls:
        if entry.value == value:
            return entry
    raise ValueError(f"{value} is not a valid value for {enum_cls.__name__}")


def get_enum_strings_from_enum(enum_cls: Type[Enum]) -> list[str]:
    return [entry.value for entry in enum_cls]
