#!/usr/bin/env python3
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import StringIO
from html.parser import HTMLParser
import textwrap, os, re
from bible import Bible

class MLStripper(HTMLParser):
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

bible = Bible('NAA')

# Lucas 16.19-31
input = 'Lucas 16.19-31'
# input = '2 Tessalonicenses 10:1-2'
# input = 'Deuteronômio 30:1-20'
# input = 'Salmos 119:110-175'

verses = bible.get_verses_by_string(input)

def clean_text(text: str) -> str:
    chars_to_remove = ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ']
    text = text.translate({ ord(x): '' for x in chars_to_remove })
    # text = re.sub(r'<\w+\/?>(.<\/\w+>)?', '', verse["text"])
    parser = MLStripper()
    parser.feed(text)
    text = parser.get_data()
    return text

# for verse in verses:
#     number = verse["verse"]
#     text = clean_text(verse["text"])
#     print(verse["verse"], text)
# exit()

# Vars
margin = 70
text_shadow_size = 3

# Fonts
font_title = ImageFont.truetype('fonts/gothic.ttf', 80)
font_versiculo = ImageFont.truetype('fonts/gothic-italic.ttf', 60)
font_body = ImageFont.truetype('fonts/gothic-bold.ttf', 80)

# Open background image
background_image = 'backgrounds/bible-classic.png'
output_dir = 'output'
output_prefix = output_dir + '/pregacao_'
img = Image.open(background_image)
draw = ImageDraw.Draw(img)

# Create output dir if not exists
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# Write text title
def write_title(draw, title):
    pos = margin
    pos_shadow = pos + text_shadow_size
    draw.text((pos_shadow, pos_shadow), title, font=font_title, fill=(0, 0, 0))
    draw.text((pos, pos), title, font=font_title, fill=(210, 186, 81))

text_title = input.upper() + ' (' + bible.version + ')' # 'LUCAS 16.1-18 (NAA)'
write_title(draw, text_title)

pos_top = margin + 150
pos_left = margin
slide = 1

for verse in verses:
    number = str(verse["verse"])
    prefix = " " * round(len(number) * 1.8) # Reserva o espaço do versiculo
    texto = prefix + clean_text(verse["text"])
    # Essa funcao corta o texto pelo tamanho de caracteres, é preciso criar outra lógica para cortar por pixels.
    texto = textwrap.fill(texto, 42)
    line_width, line_height = font_body.getsize(texto)
    text_lines = len(texto.split("\n"))
    text_height = round((line_height * text_lines)) + 40

    print("." + number + ": L: " + str(text_lines)  + " LH: " + str(line_height) + " TH: " + str(text_height) + " POS:", pos_top + text_height) 

    if ((pos_top + text_height) > 1084):
        img.save(output_prefix + str(slide) + ".png")
        # img.show()
        img = Image.open(background_image)
        draw = ImageDraw.Draw(img)
        write_title(draw, text_title)
        pos_top = margin + 150
        slide += 1

    # pos_top = pos_top + line_height
    pos_top_shadow = pos_top + text_shadow_size
    pos_left_shadow = pos_left + text_shadow_size
    draw.text((pos_left_shadow, pos_top_shadow + 20), number, font=font_versiculo, fill=(0, 0, 0))
    draw.text((pos_left, pos_top + 20), number, font=font_versiculo, fill=(210, 186, 81))
    draw.text((pos_left_shadow, pos_top_shadow), texto, font=font_body, fill=(0, 0, 0))
    draw.text((pos_left, pos_top), texto, font=font_body, fill=(255, 255, 255))
    pos_top += text_height   


# img.show()
img.save(output_prefix + str(slide) + ".png")

print('Concluded')
