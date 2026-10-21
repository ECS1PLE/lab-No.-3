from abc import ABC, abstractmethod
from pathlib import Path
from addressRecord import addressRecord

class FileParser(ABC):
    @abstractmethod
    def parse(self, path: Path) -> dict[addressRecord, int]:
        pass