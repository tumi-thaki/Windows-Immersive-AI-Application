from pathlib import Path

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textExtraction.plainTextExtractor import PlainTextExtractor
from textExtraction.wordExtractor import WordExtractor
from textExtraction.PDFExtractor import PDFExtractor
from textExtraction.powerPointExtractor import PowerPointExtractor

def get_extractor(file_path: str):
    path = Path(file_path)
    extension = path.suffix.lower()
    
    extractors = {
        '.txt': PlainTextExtractor,
        '.docx': WordExtractor,
        '.pdf': PDFExtractor,
        '.pptx': PowerPointExtractor
    }
    extractor_class = extractors.get(extension)

    if not extractor_class:
        raise ValueError(f"No extractor available for extension: {extension}")

    return extractor_class(file_path)