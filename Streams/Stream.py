
from abc import abstractmethod
from typing import Optional

class Stream:
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
        pass

    @abstractmethod
    def write(self, data) -> int:
        """
        Write data to stream

        :param data: data to write
        :return: number of bytes written
        """
        pass

    @abstractmethod
    def read(self, size: int = 1) -> Optional[bytes]:
        """
        Read data from stream

        :param size: number of bytes to read
        :return: data read
        """
        pass

    @abstractmethod
    def teardown(self) -> None:
        """
        Teardown stream

        :return: None
        """
        pass
