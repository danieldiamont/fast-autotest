"""
    Description: CCSDS Packet data structure
    Version: 1.0
    Author: Daniel Diamont
"""

import struct
from dataclasses import dataclass
from Protocols.protocol import Protocol


@dataclass
class CcsdsPacket(Protocol):
    """
    CCSDS Packet data structure.

    CCSDS Packet data structure with version, type, secondary header flag,
    APID, sequence flags, sequence count, length, payload, and checksum fields.
    """

    # pylint: disable=too-many-instance-attributes
    # The number of attributes is dictated by CCSDS.
    version: int
    type: int
    sec_header_flag: int
    apid: int
    seq_flags: int
    seq_count: int
    length: int
    payload: bytes
    checksum: int

    def serialize(self) -> bytes:
        """
        Serialize CCSDS Packet data structure to bytes

        :return: serialized data
        """

        return struct.pack('!B', self.version) + \
            struct.pack('!B', self.type) + \
            struct.pack('!B', self.sec_header_flag) + \
            struct.pack('!H', self.apid) + \
            struct.pack('!B', self.seq_flags) + \
            struct.pack('!H', self.seq_count) + \
            struct.pack('!H', self.length) + \
            self.payload + \
            struct.pack('!H', self.checksum)

    @staticmethod
    def deserialize(data: bytes) -> 'CcsdsPacket':
        """
        Deserialize bytes to CCSDS Packet data structure

        :param data: data to deserialize
        :return: deserialized data
        """

        version = struct.unpack('!B', data[0:1])[0]
        _type = struct.unpack('!B', data[1:2])[0]
        sec_header_flag = struct.unpack('!B', data[2:3])[0]
        apid = struct.unpack('!H', data[3:5])[0]
        seq_flags = struct.unpack('!B', data[5:6])[0]
        seq_count = struct.unpack('!H', data[6:8])[0]
        length = struct.unpack('!H', data[8:10])[0]
        payload = data[10:10 + length]
        checksum = struct.unpack('!H', data[10 + length:12 + length])[0]
        return CcsdsPacket(
            version,
            _type,
            sec_header_flag,
            apid,
            seq_flags,
            seq_count,
            length,
            payload,
            checksum)

    @staticmethod
    def wrap_default(payload: bytes) -> 'CcsdsPacket':
        """
        Wrap payload in default CCSDS Packet data structure

        :param payload: payload to wrap
        :return: CCSDS Packet data structure
        """

        return CcsdsPacket(0, 0, 0, 0, 0, 0, len(payload), payload, 0)
