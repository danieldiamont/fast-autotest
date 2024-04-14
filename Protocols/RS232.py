from dataclasses import dataclass
import struct

@dataclass
class RS232_MSG:
    """
    RS232 Message data structure with header, payload, and footer fields.
    """

    header: int
    payload: bytes
    footer: int

    def __bytes__(self) -> bytes:
        """
        Serialize RS232 Message data structure to bytes

        :return: serialized data
        """

        hdr = struct.pack('B', self.header)
        ftr = struct.pack('B', self.footer)
        return hdr + self.payload + ftr

    def serialize(self) -> bytes:
        """
        Serialize RS232 Message data structure to bytes

        :return: serialized data
        """

        return self.__bytes__()

    @staticmethod
    def deserialize(data: bytes) -> 'RS232_MSG':
        """
        Deserialize bytes to RS232 Message data structure

        :param data: data to deserialize
        :return: deserialized data
        """

        header = struct.unpack('B', data[0:1])[0]
        footer = struct.unpack('B', data[-1:])[0]
        payload = data[1:-1]
        return RS232_MSG(header, payload, footer)
