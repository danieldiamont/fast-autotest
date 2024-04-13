from Protocols.CCSDS import CCSDS_Packet
from Protocols.RS232 import RS232_MSG
import time

def test_serial_loopback_single_frame(serial_loopback_stream):
    # get stream fixture
    stream = serial_loopback_stream
    
    # configure and serialize message payload, CCSDS packet, and RS232_MSG
    payload = b'Hello, World!'
    expected = payload
    packet = CCSDS_Packet.wrap_default(payload).serialize()
    message = RS232_MSG(0x55, packet, 0xAA).serialize()

    # write message to stream
    stream.write(message)

    # TODO buffer read
    time.sleep(0.1)

    # read message from stream
    msg = RS232_MSG.deserialize(stream.read(len(message)))
    deserialized = CCSDS_Packet.deserialize(msg.packet).payload
    
    assert deserialized == expected
