import json
import logging
import os
import pytest

from Streams.DummyStream import DummyStream
from Streams.SerialStream import SerialStream

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

config_path = os.path.join(os.path.dirname(__file__), 'tests', 'config.json')

with open(config_path, 'r') as f:
    config = json.load(f)


@pytest.fixture
def dummy_stream():
    s = DummyStream(logger)
    yield s
    s.teardown()

@pytest.fixture
def serial_loopback_stream():
    s = SerialStream(logger, **config['serial-loopback'])
    yield s
    s.teardown()
