
from typing import Optional
from Streams.Stream import Stream


class DummyStream(Stream):
    def __init__(self, logger):
        self.logger = logger

    def write(self, data):
        self.logger.info("DummyStream: Writing data: {}".format(data.hex()))
        self.data = data
        return len(data)

    def read(self, size: int = 1) -> Optional[bytes]:
        _ = size
        self.logger.info("DummyStream: Reading data: {}".format(self.data.hex()))
        if not self.data:
            return None
        return self.data

    def teardown(self):
        self.logger.info("DummyStream: Teardown")

