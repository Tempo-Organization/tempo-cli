from enum import Enum


class SigMethodType(Enum):
    """
    Enum for the way to provide a sig when creating a mod release
    """
    NONE = 'none' # doesn't generate one
    COPY = 'copy' # copies and renames an existing one from the game install
    EMPTY = 'empty' # creates an empty file named and placed where the actual sig should be