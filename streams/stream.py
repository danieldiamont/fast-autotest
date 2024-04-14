"""
Description: Stream interface
Author: Daniel Diamont
"""

from abc import ABC, abstractmethod
from typing import Optional


class Stream(ABC):
    """
    Abstract class for stream objects

    Stream objects are used to read and write data to a stream that conforms to the Stream interface
    """

    @abstractmethod
    def setup(self, **config: Optional[dict]) -> None:
        """
        Setup stream

        :param config: configuration dictionary
        :return: None
        """

    @abstractmethod
    def write(self, data: bytes) -> int:
        """
        Write data to stream

        :param data: data to write
        :return: number of bytes written
        """

    @abstractmethod
    def read(self, size: int = 1) -> Optional[bytes]:
        """
        Read data from stream

        :param size: number of bytes to read
        :return: data read
        """

    @abstractmethod
    def teardown(self) -> None:
        """
        Teardown stream

        :return: None
        """
