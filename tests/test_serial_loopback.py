from Protocols.CCSDS import CCSDS_Packet
from Protocols.RS232 import RS232_MSG
import time

def test_serial_loopback(serial_loopback_stream):
    """
    Test serial loopback stream by writing and reading messages.

    Each message is a RS232_MSG object that contains a CCSDS packet with a custom payload.

    :param serial_loopback_stream: SerialStream object
    :return: None
    """
    stream = serial_loopback_stream

    payloads = [b'Hello, World!', b'Goodbye, World!']
    expected = payloads

    # configure and serialize message payload, CCSDS packet, and RS232_MSG
    messages = []
    for payload in payloads:
        packet = CCSDS_Packet.wrap_default(payload).serialize()
        message = RS232_MSG(0x55, packet, 0xAA).serialize()
        messages.append(message)

    # write messages to stream
    for message in messages:
        stream.write(message)
        time.sleep(0.1)

    # read messages from stream
    msgs = []
    for message in messages:
        msgs.append(RS232_MSG.deserialize(stream.read(len(message))))

    deserialized = [CCSDS_Packet.deserialize(msg.packet).payload for msg in msgs]

    print(f"Actual: {deserialized}\t Expected: {expected}")
    assert deserialized == expected

