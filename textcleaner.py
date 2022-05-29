from io import StringIO
from html.parser import HTMLParser

class TextCleaner(HTMLParser):
    # Inspired by: https://stackoverflow.com/a/925630/777755
    # Usage: TextCleaner.clean_text(...)
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()
    
    @classmethod
    def clean_text(cls, text: str) -> str:
        chars_to_remove = ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ']
        text = text.translate({ ord(x): '' for x in chars_to_remove })
        # text = re.sub(r'<\w+\/?>(.<\/\w+>)?', '', verse["text"])
        parser = cls()
        parser.feed(text)
        text = parser.get_data()
        return text
