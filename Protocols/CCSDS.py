from dataclasses import dataclass
import struct

@dataclass
class CCSDS_Packet:
    version: int
    type: int
    sec_header_flag: int
    apid: int
    seq_flags: int
    seq_count: int
    length: int
    payload: bytes
    checksum: int

    def __bytes__(self):
        return struct.pack('!B', self.version) + \
               struct.pack('!B', self.type) + \
               struct.pack('!B', self.sec_header_flag) + \
               struct.pack('!H', self.apid) + \
               struct.pack('!B', self.seq_flags) + \
               struct.pack('!H', self.seq_count) + \
               struct.pack('!H', self.length) + \
               self.payload + \
               struct.pack('!H', self.checksum)

    def serialize(self):
        return self.__bytes__()

    @staticmethod
    def deserialize(data: bytes) -> 'CCSDS_Packet':
        version = struct.unpack('!B', data[0:1])[0]
        type = struct.unpack('!B', data[1:2])[0]
        sec_header_flag = struct.unpack('!B', data[2:3])[0]
        apid = struct.unpack('!H', data[3:5])[0]
        seq_flags = struct.unpack('!B', data[5:6])[0]
        seq_count = struct.unpack('!H', data[6:8])[0]
        length = struct.unpack('!H', data[8:10])[0]
        payload = data[10:10+length]
        checksum = struct.unpack('!H', data[10+length:12+length])[0]
        return CCSDS_Packet(version, type, sec_header_flag, apid, seq_flags, seq_count, length, payload, checksum)

    @staticmethod
    def wrap_default(payload: bytes) -> 'CCSDS_Packet':
        return CCSDS_Packet(0, 0, 0, 0, 0, 0, len(payload), payload, 0)
