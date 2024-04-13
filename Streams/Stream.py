from abc import abstractmethod
from typing import Optional

class Stream:
    @abstractmethod
    def write(self, data) -> int:
        pass

    @abstractmethod
    def read(self, size: int = 1) -> Optional[bytes]:
        pass

    @abstractmethod
    def teardown(self):
        pass
