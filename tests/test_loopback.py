
def test_loopback(dummy_stream):
    stream = dummy_stream
    stream.write(b'Hello')
    assert stream.read() == b'Hello'
