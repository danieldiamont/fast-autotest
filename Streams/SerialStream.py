import time
import serial
from Streams.Stream import Stream
from typing import Optional

class SerialStream(Stream):
    def __init__(self, logger, **config: dict) -> None:
        self.logger = logger
        self.setup(**config)


    def setup(self, **config: dict) -> None:
        tx_config = config['TX']
        rx_config = config['RX']
        try:
            self.tx = serial.Serial(**tx_config)
            self.rx = serial.Serial(**rx_config)
            time.sleep(0.5)
        except serial.SerialException as e:
            self.logger.error("Error: Could not open serial port: {}".format(e))
            raise e
        except ValueError as e:
            self.logger.error("Error: Invalid serial port or options: {}".format(e))
            raise e
        finally:
            self.logger.info("SerialStream: Setup complete")
        
    def teardown(self) -> None:
        if self.tx:
            self.tx.close()
        if self.rx:
            self.rx.close()


    def read(self, size: int = 1) -> Optional[bytes]:
        if self.rx:
            try:
                data = self.rx.read(size)
                
                self.logger.info("SerialStream - Reading data: {}".format(data.hex()))
                return data
            except serial.SerialTimeoutException as e:
                self.logger.error("Timeout error: {}".format(e))
        return None

    def write(self, data: bytes) -> int:
        if self.tx:
            try:
                ret = self.tx.write(data)
                
                self.logger.info("SerialStream: Writing data: {}".format(data.hex()))
                
                if not ret or ret < 0 or ret != len(data):
                    self.logger.error("SerialStream: Write error: {}".format(ret))
                    return -1
                
                return ret
            except serial.SerialTimeoutException as e:
                self.logger.error("Timeout error: {}".format(e))
            except serial.PortNotOpenError as e:
                self.logger.error("Port not open: {}".format(e))
        return -1
