"""
    Description: Test dummy stream loopback by writing and reading messages.
    Author: Daniel Diamont
"""

def test_loopback(dummy_stream):
    """
    Test dummy stream loopback by writing and reading messages.

    :param dummy_stream: DummyStream fixture
    :return: None
    """
    stream = dummy_stream
    stream.write(b'Hello')
    assert stream.read() == b'Hello'
