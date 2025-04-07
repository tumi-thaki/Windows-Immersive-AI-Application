from .baseExtractor import TextExtractor

class PlainTextExtractor(TextExtractor):
    def extract_text(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return self.clean_text(text)