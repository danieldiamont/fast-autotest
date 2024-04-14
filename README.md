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

The framework is designed to be modular and extensible. The framework is composed of the following components:
- Streams
- Protocols
- Tests
- config.json
- Fixtures

### Streams

Streams are the core of the framework. A stream is a wrapper around a data resource that provides an interface for reading and writing data as well as executing setup and teardown operations specific to the data source.

Specifically, the framework provides a Stream abstract base class that defines the interface for a data stream. A Stream subclass must implement the following abstract methods:

- `setup(self, **config: Optional[dict]) -> None`: Set up the stream.
- `write(self, data: bytes) -> int`: Write data to the stream. Returns the number of bytes written.
- `read(self, size: int) -> Optional[bytes]`: Read data from the stream. Returns the data read or None if no data is available.
- `teardown(self) -> None`: Clean up the stream.

See `Streams/SerialStream.py` for an example of a Stream subclass for serial port communications.

### Protocols

Protocols are data structures that define the format of data packets.


### Fixtures

Fixtures are used to create and managed Streams. Fixtures are defined in `tests/conftest.py`.


### config.json

The `config.json` file is used to specify the configuration for the tests. For example, for a serial-loopback test, the configuration file specifies the serial ports used for the loopback, as well as the baud rate and other serial port settings.

Configuration of this file goes hand in hand with `tests/conftest.py`, which parses the `config.json` file and creates fixtures for the tests accordingly.


### Tests

Tests are defined in the `tests` directory. Each test can take a stream fixture as an input. The test can then use the stream fixture to read and write data to the stream and perform assertions on the data.

Tests defined in this manner are automatically detected by the pytest framework, which will inject the appopriate fixtures into the test functions at runtime.


## Demo

To run the demo, execute the following command:

```
./start_serial_loopback.sh
```

This will start a socat process that will loopback a serial port to itself. The demo uses `tests/config.json` to specifiy the serial ports used for the loopbock. If the ports in config.json are different than what socat is outputting, run:
```
python3 demo-update-ports.py <port1> <port2>
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


