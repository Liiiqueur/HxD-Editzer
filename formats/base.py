from abc import ABC, abstractmethod

class FileFormatAnalyzer(ABC):
    name = ""
    signatures = []
    color = "#FFFFFF"

    def detect(self, data: bytes) -> bool:
        return any(
            data.startswith(bytes.fromhex(sig))
            for sig in self.signatures
        )

    @abstractmethod
    def extract_metadata(self, data: bytes) -> dict:
        pass
