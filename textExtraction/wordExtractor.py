import docx
from .baseExtractor import TextExtractor

class WordExtractor(TextExtractor):
    def extract_text(self) -> str:
        doc = docx.Document(self.file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return self.clean_text(text)