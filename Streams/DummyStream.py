
from typing import Optional
from Streams.Stream import Stream


class DummyStream(Stream):
    """
    Dummy stream object for demonstration purposes as a stream loopback.
    """

    def __init__(self, logger) -> None:
        """
        Initialize DummyStream object

        :param logger: logger object
        :return: None
        """

        self.logger = logger
        self.setup()


    def setup(self, **config: Optional[dict]) -> None:
        """
        Setup stream

        :param config: configuration dictionary
        :return: None
        """

        self.data = None
        _ = config
        self.logger.info("DummyStream: Setup complete")


    def write(self, data: bytes) -> int:
        """
        Write data to stream

        :param data: data to write
        :return: number of bytes written
        """

        self.logger.info("DummyStream: Writing data: {}".format(data.hex()))
        self.data = data
        return len(data)


    def read(self, size: int = 1) -> Optional[bytes]:
        """
        Read data from stream

        :param size: number of bytes to read
        :return: data read
        """

        _ = size

        if not self.data:
            self.logger.error("DummyStream: No data to read")
            return None

        self.logger.info("DummyStream: Reading data: {}".format(self.data.hex()))
        return self.data


    def teardown(self) -> None:
        """
        Teardown stream

        :return: None
        """

        self.logger.info("DummyStream: Teardown")

