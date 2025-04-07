from pathlib import Path
from .plainTextExtractor import PlainTextExtractor
from .wordExtractor import WordExtractor
from .PDFExtractor import PDFExtractor
from .powerPointExtractor import PowerPointExtractor

def get_extractor(file_path: str):
    file_path = Path(file_path)
    extension = file_path.suffix.lower()
    
    extractors = {
        '.txt': PlainTextExtractor,
        '.docx': WordExtractor,
        '.pdf': PDFExtractor,
        '.pptx': PowerPointExtractor
    }
    