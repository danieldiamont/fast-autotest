# fast-autotest

## Description

This is a simple test automation framework originally intended to CCSDS packets sent over serial. However, after refactoring fixtures to manufacture Streams, it can be used to test any kind of data stream that implements the abstract methods in the Stream abstract base class.


## Installation

To install the required dependencies for the framework only, I recommend creating a virtual environment and installing the dependencies from `requirements.txt`. To install the dependencies for the demo, you will need to install socat.

```
pip install -r requirements.txt

sudo apt-get install socat
```

## Architecture

### Streams

The framework is designed to test data streams. A data stream is a sequence of data packets. The framework provides a Stream abstract base class that defines the interface for a data stream. A Stream subclass must implement the following abstract methods:

- `write(self, data: bytes) -> int`: Write data to the stream. Returns the number of bytes written.
- `read(self, size: int) -> Optional[bytes]`: Read data from the stream. Returns the data read or None if no data is available.
- `teardown(self) -> None`: Clean up the stream.

### Protocols

## Demo

To run the demo, execute the following command:

```
./start_serial_loopback.sh
```

This will start a socat process that will loopback a serial port to itself. The demo uses `tests/config.json` to specifiy the serial ports used for the loopbock. If the ports in config.json are different than what socat is outputting, run:
```
python3 update_ports.py
```

Then, execute the following command:

```
pytest -v
```

## Extending Streams

To extend the framework to test a new kind of data stream, create a new class that inherits from the Stream abstract base class. Implement the abstract methods in the Stream class. Then, create your own fixture using your Stream subclass. See SerialStream and stream_fixture in tests/conftest.py for an example.

## Protocols

The framework currently supports the following protocols:
- CCSDS packets
- Raw bytes data with start and stop bytes

The framework is designed to easily compose protocols. For example, a CCSDS packet be embedded within an RS232_MSG by serializing the CCSDS_Packet as the RS232_MSG's payload. Additionally, the framework is designed to be easily extensible to support new protocols. To add a new protocol, create a `@dataclass` that represents the protocol's packet structure and add serialization and deserialization (to/from bytes).

## Contributing

To contribute to this project, fork the repository and create a new branch. Then, submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


