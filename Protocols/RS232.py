from dataclasses import dataclass
import struct

@dataclass
class RS232_MSG:
    header: int
    packet: bytes
    footer: int

    def __bytes__(self):
        hdr = struct.pack('B', self.header)
        ftr = struct.pack('B', self.footer)
        return hdr + self.packet + ftr

    def serialize(self):
        return self.__bytes__()

    @staticmethod
    def deserialize(data: bytes) -> 'RS232_MSG':
        header = struct.unpack('B', data[0:1])[0]
        footer = struct.unpack('B', data[-1:])[0]
        packet = data[1:-1]
        return RS232_MSG(header, packet, footer)
