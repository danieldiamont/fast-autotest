from dataclasses import dataclass
import time
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

@dataclass
class Message:
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
    def deserialize(data: bytes) -> 'Message':
        header = struct.unpack('B', data[0:1])[0]
        footer = struct.unpack('B', data[-1:])[0]
        packet = data[1:-1]
        return Message(header, packet, footer)



def test_serial_loopback_single_frame(serial_loopback_stream):
    # get stream fixture
    stream = serial_loopback_stream
    
    # configure and serialize message payload, CCSDS packet, and Message
    payload = b'Hello, World!'
    expected = payload
    packet = CCSDS_Packet.wrap_default(payload).serialize()
    message = Message(0x55, packet, 0xAA).serialize()

    # write message to stream
    stream.write(message)

    # TODO buffer read
    time.sleep(0.1)

    # read message from stream
    msg = Message.deserialize(stream.read(len(message)))
    deserialized = CCSDS_Packet.deserialize(msg.packet).payload
    
    assert deserialized == expected
