"""
Description: SerialStream class for reading and writing data through a serial port.
Author: Daniel Diamont
"""

import time
from typing import Optional
import serial
from streams.stream import Stream


class SerialStream(Stream):
    """
    Serial stream object for reading and writing data through a serial port.
    """

    def __init__(self, logger, **config: dict) -> None:
        """
        Initialize SerialStream object

        :param logger: logger object
        :param config: configuration dictionary
        :return: None
        """

        self.logger = logger
        self.setup(**config)

    def setup(self, **config: dict) -> None:
        """
        Setup serial stream

        :param config: configuration dictionary
        :return: None
        """

        tx_config = config['TX']
        rx_config = config['RX']
        try:
            self._tx = serial.Serial(**tx_config)
            self._rx = serial.Serial(**rx_config)
            time.sleep(0.5)
        except serial.SerialException as exception:
            self.logger.error(
                f"Error: Could not open serial port: {exception}")
            raise exception
        except ValueError as exception:
            self.logger.error(
                f"Error: Invalid serial port or options: {exception}")
            raise exception
        finally:
            self.logger.info("SerialStream: Setup complete")

    def teardown(self) -> None:
        """
        Teardown serial stream

        :return: None
        """

        if self._tx:
            self._tx.close()
        if self._rx:
            self._rx.close()

    def read(self, size: int = 1) -> Optional[bytes]:
        """
        Read data from serial stream

        :param size: number of bytes to read
        :return: data read
        """

        if self._rx:
            try:
                data = self._rx.read(size)

                self.logger.info(
                    f"SerialStream - Reading data: {data.hex()}")
                return data
            except serial.SerialTimeoutException as exception:
                self.logger.error(f"Timeout error: {exception}")
        return None

    def write(self, data: bytes) -> int:
        """
        Write data to serial stream

        :param data: data to write
        :return: number of bytes written
        """

        if self._tx:
            try:
                ret = self._tx.write(data)

                self.logger.info(
                    f"SerialStream: Writing data: {data.hex()}"
                    )

                if not ret or ret < 0 or ret != len(data):
                    self.logger.error(
                        f"SerialStream: Write error: {ret}")
                    return -1

                return ret
            except serial.SerialTimeoutException as exception:
                self.logger.error(f"Timeout error: {exception}")
            except serial.PortNotOpenError as exception:
                self.logger.error(f"Port not open: {exception}")
        return -1
