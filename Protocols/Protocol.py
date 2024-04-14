from abc import ABC, abstractmethod

class Protocol(ABC):
    """
    Protocol data structure with payload field.
    """

    payload: bytes

    @abstractmethod
    def serialize(self) -> bytes:
        """
        Serialize Protocol data structure to bytes

        :return: serialized data
        """

        pass


    @classmethod
    @abstractmethod
    def deserialize(cls, data: bytes) -> 'Protocol':
        """
        Deserialize bytes to Protocol data structure

        :param data: data to deserialize
        :return: deserialized data
        """
        pass
