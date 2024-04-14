"""
    Description: Test serial loopback stream by writing and reading messages.
    Author: Daniel Diamont
"""

import time
from Protocols.ccsds import CcsdsPacket
from Protocols.rs232 import Rs232Msg


def test_serial_loopback(serial_loopback_stream):
    """
    Test serial loopback stream by writing and reading messages.

    Each message is a Rs232Msg object that contains a CCSDS packet with a custom payload.

    :param serial_loopback_stream: SerialStream fixture
    :return: None
    """
    stream = serial_loopback_stream

    payloads = [b'Hello, World!', b'Goodbye, World!']
    expected = payloads

    # configure and serialize message payload, CCSDS packet, and Rs232Msg
    messages = []
    for payload in payloads:
        serial_payload = CcsdsPacket.wrap_default(payload).serialize()
        message = Rs232Msg(0x55, serial_payload, 0xAA).serialize()
        messages.append(message)

    # write messages to stream
    for message in messages:
        stream.write(message)
        time.sleep(0.1)

    # read messages from stream
    msgs = []
    for message in messages:
        msgs.append(Rs232Msg.deserialize(stream.read(len(message))))

    deserialized = [CcsdsPacket.deserialize(
        msg.payload).payload for msg in msgs]

    print(f"Actual: {deserialized}\t Expected: {expected}")
    assert deserialized == expected
