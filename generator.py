from PIL import Image, ImageDraw, ImageFont
from bible import Bible
from theme import Theme
from textcleaner import TextCleaner
from threading import Timer
import textwrap, webbrowser, os

class Generator:
    def __init__(self, bible: Bible, theme: Theme):
        self.bible = bible
        self.theme = theme
        self.margin = self.theme.getparam('margin', 70)
        self.body_start_position = self.theme.getparam('body_start_position', 150)
        self.chars_per_line = self.theme.getparam('chars_per_line', 40)
        self.text_shadow_size = 3
        self.slides = []
        self.cursor_pos_top = 0
        self.cursor_pos_left = 0
        self.debug = False

    @property
    def base_image(self):
        return self.theme.background

    @property
    def font_title(self):
        return ImageFont.truetype(self.theme.getstylefont('title'), self.theme.getstylesize('title'))

    @property
    def font_number(self):
        return ImageFont.truetype(self.theme.getstylefont('number'), self.theme.getstylesize('number'))

    @property
    def font_verse(self):
        return ImageFont.truetype(self.theme.getstylefont('body'), self.theme.getstylesize('body'))

    def generate(self, bibleText: str):
        # Generate Texts
        verses = self.bible.get_verses_by_string(bibleText)
        img = Image.open(self.base_image)
        draw = ImageDraw.Draw(img)
        text_title = bibleText.upper() + ' (' + self.bible.version + ')'
        self.writetitle(draw, text_title)
        self.cursor_pos_top = self.margin + self.body_start_position
        self.cursor_pos_left = self.margin
        
        if self.debug:
            print("-> Generating Text for %s..." % bibleText)

        for verse in verses:
            number = str(verse["verse"])
            prefix = " " * round(len(number) * 1.8) # Reserva o espaço do versiculo
            texto = prefix + TextCleaner.clean_text(verse["text"])
            # Essa funcao corta o texto pelo tamanho de caracteres, é preciso criar outra lógica para cortar por pixels.
            texto = textwrap.fill(texto, self.chars_per_line)
            line_width, line_height = self.font_verse.getsize(texto)
            text_lines = len(texto.split("\n"))
            text_height = round((line_height * text_lines)) + 40
            
            if self.debug:
                print("." + number + ": L: " + str(text_lines)  + " LH: " + str(line_height) + " TH: " + str(text_height) + " POS:", self.cursor_pos_top + text_height) 
            
            if ((self.cursor_pos_top + text_height) > 1084):
                self.slides.append(img)
                img = Image.open(self.base_image)
                draw = ImageDraw.Draw(img)
                self.writetitle(draw, text_title)
                self.cursor_pos_top = self.margin + self.body_start_position
            
            self.writetext(draw, number, texto)
            self.cursor_pos_top += text_height

        self.slides.append(img)

        return self

    def writetitle(self, draw: ImageDraw, title: str):
        pos = self.margin
        pos_shadow = pos + self.text_shadow_size
        draw.text((pos_shadow, pos_shadow),
                  title,
                  font=self.font_title,
                  fill=(0, 0, 0))
        draw.text((pos, pos),
                  title,
                  font=self.font_title,
                  fill=self.theme.getstylecolor('title')) #fill=(210, 186, 81))

    def writetext(self, draw: ImageDraw, number: str, text: str):
        pos_top_shadow = self.cursor_pos_top + self.text_shadow_size
        pos_left_shadow = self.cursor_pos_left + self.text_shadow_size
        draw.text((pos_left_shadow, pos_top_shadow + 20),
                  number,
                  font=self.font_number,
                  fill=(0, 0, 0))
        draw.text((self.cursor_pos_left, self.cursor_pos_top + 20),
                  number,
                  font=self.font_number,
                  fill=self.theme.getstylecolor('number'))
        draw.text((pos_left_shadow, pos_top_shadow),
                  text,
                  font=self.font_verse,
                  fill=(0, 0, 0))
        draw.text((self.cursor_pos_left, self.cursor_pos_top),
                  text,
                  font=self.font_verse,
                  fill=self.theme.getstylecolor('body'))
        
    def save(self, output_dir: str = './output'):
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
    
        for i, slide in enumerate(self.slides):
            if self.debug:
                print("Saving slide %s..." % str(i + 1))

            slide.save("%s/pregacao%s.png" % (output_dir, str(i + 1)))
            
    def opendir(self, path: str):
        def open():
            webbrowser.open('file:///' + os.path.realpath(path))

        Timer(1, open).start()

    def clear(self):
        self.slides = []
