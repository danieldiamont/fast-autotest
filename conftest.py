"""
Description: Module to configure the test environment and fixtures
Author: Daniel Diamont
"""


import json
import logging
import os
import pytest

from streams.dummy_stream import DummyStream
from streams.serial_stream import SerialStream

# logging
FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    filename='log.txt',
    filemode='w',
    encoding='utf-8',
    format=FORMAT
)


# load configuration
config_path = os.path.join(os.path.dirname(__file__), 'tests', 'config.json')
with open(config_path, 'r', encoding="utf-8") as file:
    config = json.load(file)


# fixtures
@pytest.fixture
def dummy_stream():
    """
    Fixture to create a DummyStream object
    """

    stream = DummyStream(logger)
    yield stream
    stream.teardown()


@pytest.fixture
def serial_loopback_stream():
    """
    Fixture to create a SerialStream object
    """
    stream = SerialStream(logger, **config['serial-loopback'])
    yield stream
    stream.teardown()
