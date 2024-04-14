from dataclasses import dataclass
from Protocols.Protocol import Protocol
import struct

@dataclass
class RS232_MSG(Protocol):
    """
    RS232 Message data structure with header, payload, and footer fields.
    """

    header: int
    payload: bytes
    footer: int

    def serialize(self) -> bytes:
        """
        Serialize RS232 Message data structure to bytes

        :return: serialized data
        """

        hdr = struct.pack('B', self.header)
        ftr = struct.pack('B', self.footer)
        return hdr + self.payload + ftr


    @classmethod
    def deserialize(cls, data: bytes) -> 'RS232_MSG':
        """
        Deserialize bytes to RS232 Message data structure

        :param data: data to deserialize
        :return: deserialized data
        """

        header = struct.unpack('B', data[0:1])[0]
        footer = struct.unpack('B', data[-1:])[0]
        payload = data[1:-1]
        return RS232_MSG(header, payload, footer)
