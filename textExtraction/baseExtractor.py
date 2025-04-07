from abc import ABC, abstractmethod
from pathlib import Path

class TextExtractor(ABC):
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
    
    @abstractmethod
    def extract_text(self) -> str:
        pass
    
    def clean_text(self, text: str) -> str:
        return " ".join(text.split())
    
    def save_text(self, output_path: str, text: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)