from abc import ABC, abstractmethod

class Protocol(ABC):
    """
    Protocol data structure with payload field.
    """

    payload: bytes

    @abstractmethod
    def __bytes__(self) -> bytes:
        """
        Serialize Protocol data structure to bytes

        :return: serialized data
        """

        pass
