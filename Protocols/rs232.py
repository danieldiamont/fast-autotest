"""
    Description: RS232 Protocol data structure with header, payload, and footer fields.
    Version: 1.0
    Author: Daniel Diamont
"""


import struct
from dataclasses import dataclass
from Protocols.protocol import Protocol


@dataclass
class Rs232Msg(Protocol):
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

    @staticmethod
    def deserialize(data: bytes) -> 'Rs232Msg':
        """
        Deserialize bytes to RS232 Message data structure

        :param data: data to deserialize
        :return: deserialized data
        """

        header = struct.unpack('B', data[0:1])[0]
        footer = struct.unpack('B', data[-1:])[0]
        payload = data[1:-1]
        return Rs232Msg(header, payload, footer)
