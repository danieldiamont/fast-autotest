"""
Description: Protocol data structure with serialize and deserialize abstract methods
Author: Daniel Diamont
"""

from abc import ABC, abstractmethod


class Protocol(ABC):
    """
    Protocol data structure with payload field.
    """

    @abstractmethod
    def serialize(self) -> bytes:
        """
        Serialize Protocol data structure to bytes

        :return: serialized data
        """

    @staticmethod
    @abstractmethod
    def deserialize(data: bytes) -> 'Protocol':
        """
        Deserialize bytes to Protocol data structure

        :param data: data to deserialize
        :return: deserialized data
        """
