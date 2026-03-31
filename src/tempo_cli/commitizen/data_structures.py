from enum import Enum
from typing import Type, Any


class CommitizenVersionSchemeOption(Enum):
    """
    Enum for the available version scheme options for Commitizen
    """
    SEMVER = 'semver'
    SEMVER2 = 'semver2'
    PEP440 = 'pep440'


def get_enum_from_val(enum_cls: Type[Enum], value: Any) -> Enum:
    for entry in enum_cls:
        if entry.value == value:
            return entry
    raise ValueError(f"{value} is not a valid value for {enum_cls.__name__}")


def get_enum_from_val_loose(enum_cls: Type[Enum], value: Any) -> Enum | None:
    for entry in enum_cls:
        if entry.value == value:
            return entry
    return None


def get_enum_strings_from_enum(enum_cls: Type[Enum]) -> list[str]:
    return [entry.value for entry in enum_cls]
