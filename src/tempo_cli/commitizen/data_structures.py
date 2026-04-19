from enum import Enum
from typing import Type, TypeVar


class CommitizenVersionSchemeOption(Enum):
    """
    Enum for the available version scheme options for Commitizen
    """
    SEMVER = 'semver'
    SEMVER2 = 'semver2'
    PEP440 = 'pep440'


E = TypeVar("E", bound=Enum)

def get_enum_from_val(enum_cls: Type[E], value: object) -> E:
    for entry in enum_cls:
        if entry.value == value:
            return entry
    raise ValueError(f"{value} is not a valid value for {enum_cls.__name__}")


def get_enum_strings_from_enum(enum_cls: Type[Enum]) -> list[str]:
    return [entry.value for entry in enum_cls]
