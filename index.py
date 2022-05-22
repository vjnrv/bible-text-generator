#!/usr/bin/env python3
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap, os

# Vars
margin = 70
text_shadow_size = 3

# Fonts
font_title = ImageFont.truetype('fonts/gothic.ttf', 80)
font_versiculo = ImageFont.truetype('fonts/gothic-italic.ttf', 60)
font_body = ImageFont.truetype('fonts/gothic-bold.ttf', 80)

# Open background image
background_image = 'backgrounds/green-sky.png'
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

versiculos = [
    {"versiculo": "1", "texto": "Depois dessas coisas, Jesus atravessou o mar da Galileia, que é o de Tiberíades. " },
    {"versiculo": "2", "texto": "Uma grande multidão o seguia, porque tinham visto os sinais que ele fazia na cura dos enfermos. " },
    {"versiculo": "3", "texto": "Então Jesus subiu ao monte e sentou-se ali com os seus discípulos. " },
    {"versiculo": "4", "texto": "Ora, a Páscoa, festa dos judeus, estava próxima. " },
    {"versiculo": "5", "texto": "Então Jesus, erguendo os olhos e vendo que uma grande multidão se aproximava, disse a Filipe: — Onde compraremos pão para lhes dar de comer? " },
    {"versiculo": "6", "texto": "Mas Jesus dizia isto para testá-lo, porque sabia o que estava para fazer. " },
    {"versiculo": "7", "texto": "Filipe respondeu: — Nem mesmo duzentos denários de pão seriam suficientes para que cada um recebesse um pedaço. " },
    {"versiculo": "8", "texto": "Um dos discípulos, chamado André, irmão de Simão Pedro, disse a Jesus: " },
    {"versiculo": "9", "texto": "— Aqui está um menino que tem cinco pães de cevada e dois peixinhos. Mas o que é isto para tanta gente? " },
    {"versiculo": "10", "texto": "Jesus disse: — Façam com que todos se assentem no chão. Havia muita relva naquele lugar. Assim, os homens se assentaram, e eram quase cinco mil. " },
    {"versiculo": "11", "texto": "Então Jesus pegou os pães e, tendo dado graças, distribuiu-os entre eles; e também igualmente os peixes, tanto quanto queriam. " },
    {"versiculo": "12", "texto": "E, quando já estavam satisfeitos, Jesus disse aos seus discípulos: — Recolham os pedaços que sobraram, para que nada se perca. " },
    {"versiculo": "13", "texto": "Assim, pois, o fizeram e encheram doze cestos de pedaços dos cinco pães de cevada, que sobraram depois que todos tinham comido. " },
    {"versiculo": "14", "texto": "Quando as pessoas viram o sinal que Jesus havia feito, disseram: — Este é verdadeiramente o profeta que devia vir ao mundo. " },
    {"versiculo": "15", "texto": "Jesus ficou sabendo que estavam para vir com a intenção de fazê-lo rei à força. Então ele se retirou outra vez, sozinho, para o monte. " },
    {"versiculo": "16", "texto": "Ao final do dia, os discípulos de Jesus desceram para o mar. " },
    {"versiculo": "17", "texto": "E, entrando num barco, passaram para o outro lado, rumo a Cafarnaum. Já estava escuro, e Jesus ainda não tinha ido até onde eles estavam. " },
    {"versiculo": "18", "texto": "E o mar começava a ficar agitado, porque soprava um vento forte. " },
    {"versiculo": "19", "texto": "Os discípulos já tinham navegado uns cinco ou seis quilômetros, quando viram Jesus andando sobre o mar, aproximando-se do barco; e ficaram com medo. " },
    {"versiculo": "20", "texto": "Mas Jesus lhes disse: — Sou eu. Não tenham medo! " },
    {"versiculo": "21", "texto": "Então eles o receberam com alegria, e logo o barco chegou ao seu destino." },
    {"versiculo": "22", "texto": "No dia seguinte, a multidão que tinha ficado do outro lado do mar notou que ali havia apenas um pequeno barco e que Jesus não tinha entrado nele com os seus discípulos, tendo estes partido sozinhos. " },
    {"versiculo": "23", "texto": "Entretanto, outros barquinhos de Tiberíades se aproximaram do lugar onde a multidão havia comido o pão depois que o Senhor deu graças. " },
    {"versiculo": "24", "texto": "Quando aquela multidão viu que Jesus não estava ali nem os seus discípulos, entraram nos barcos e partiram para Cafarnaum à procura de Jesus. " },
    {"versiculo": "25", "texto": "E, tendo-o encontrado no outro lado do mar, lhe perguntaram: — Mestre, quando o senhor chegou aqui? " },
    {"versiculo": "26", "texto": "Jesus respondeu: — Em verdade, em verdade lhes digo que vocês estão me procurando não porque viram sinais, mas porque comeram os pães e ficaram satisfeitos. " },
    {"versiculo": "27", "texto": "Trabalhem, não pela comida que se estraga, mas pela que permanece para a vida eterna, a qual o Filho do Homem dará a vocês; porque Deus, o Pai, o confirmou com o seu selo. " },
    {"versiculo": "28", "texto": "Então lhe perguntaram: — Que faremos para realizar as obras de Deus? " },
    {"versiculo": "29", "texto": "Jesus respondeu: — A obra de Deus é esta: que vocês creiam naquele que ele enviou.  " },
    {"versiculo": "30", "texto": "Então eles disseram: — Que sinal o senhor fará para que vejamos e creiamos no senhor? O que o senhor pode fazer? " },
    {"versiculo": "31", "texto": "Nossos pais comeram o maná no deserto, como está escrito: “Deu-lhes a comer pão do céu.” " },
    {"versiculo": "32", "texto": "Jesus lhes disse: — Em verdade, em verdade lhes digo que não foi Moisés quem deu o pão do céu para vocês; quem lhes dá o verdadeiro pão do céu é meu Pai. " },
    {"versiculo": "33", "texto": "Porque o pão de Deus é o que desce do céu e dá vida ao mundo. " },
    {"versiculo": "34", "texto": "Então lhe disseram: — Senhor, dê-nos sempre desse pão. " },
    {"versiculo": "35", "texto": "Jesus respondeu: — Eu sou o pão da vida. Quem vem a mim jamais terá fome, e quem crê em mim jamais terá sede. " },
    {"versiculo": "36", "texto": "Porém eu já disse que vocês não creem, embora estejam me vendo.  " },
    {"versiculo": "37", "texto": "Todo aquele que o Pai me dá, esse virá a mim; e o que vem a mim, de modo nenhum o lançarei fora. " },
    {"versiculo": "38", "texto": "Porque eu desci do céu, não para fazer a minha própria vontade, mas a vontade daquele que me enviou. " },
    {"versiculo": "39", "texto": "E a vontade de quem me enviou é esta: que eu não perca nenhum de todos os que ele me deu; pelo contrário, eu o ressuscitarei no último dia. " },
    {"versiculo": "40", "texto": "De fato, a vontade de meu Pai é que todo aquele que vir o Filho e nele crer tenha a vida eterna; e eu o ressuscitarei no último dia. " },
    {"versiculo": "41", "texto": "Então os judeus começaram a murmurar contra ele, porque tinha dito: “Eu sou o pão que desceu do céu.” " },
    {"versiculo": "42", "texto": "E diziam: — Este não é Jesus, o filho de José? Por acaso não conhecemos o pai e a mãe dele? Como é que ele agora diz: “Desci do céu”? " },
    {"versiculo": "43", "texto": "Jesus respondeu: — Não fiquem murmurando entre vocês. " },
    {"versiculo": "44", "texto": "Ninguém pode vir a mim se o Pai, que me enviou, não o trouxer; e eu o ressuscitarei no último dia. " },
    {"versiculo": "45", "texto": "Está escrito nos Profetas: “E todos serão ensinados por Deus.” Portanto, todo aquele que ouviu e aprendeu do Pai, esse vem a mim. " },
    {"versiculo": "46", "texto": "Não que alguém tenha visto o Pai, a não ser aquele que vem de Deus; este já viu o Pai. " },
    {"versiculo": "47", "texto": " — Em verdade, em verdade lhes digo: quem crê em mim tem a vida eterna. " },
    {"versiculo": "48", "texto": "Eu sou o pão da vida. " },
    {"versiculo": "49", "texto": "Os pais de vocês comeram o maná no deserto e morreram. " },
    {"versiculo": "50", "texto": "Este é o pão que desce do céu, para que todo o que dele comer não pereça. " },
    {"versiculo": "51", "texto": "Eu sou o pão vivo que desceu do céu; se alguém comer deste pão, viverá eternamente. E o pão que eu darei pela vida do mundo é a minha carne. " },
    {"versiculo": "52", "texto": "Então os judeus começaram a discutir entre si, dizendo: — Como é que este pode nos dar a sua própria carne para comer? " },
    {"versiculo": "53", "texto": "Jesus respondeu: — Em verdade, em verdade lhes digo que, se vocês não comerem a carne do Filho do Homem e não beberem o seu sangue, não terão vida em vocês mesmos. " },
    {"versiculo": "54", "texto": "Quem come a minha carne e bebe o meu sangue tem a vida eterna, e eu o ressuscitarei no último dia." },
    {"versiculo": "55", "texto": "Pois a minha carne é verdadeira comida, e o meu sangue é verdadeira bebida. " },
    {"versiculo": "56", "texto": "Quem come a minha carne e bebe o meu sangue permanece em mim, e eu permaneço nele. " },
    {"versiculo": "57", "texto": "Assim como o Pai, que vive, me enviou, e igualmente eu vivo por causa do Pai, também quem de mim se alimenta viverá por mim. " },
    {"versiculo": "58", "texto": "Este é o pão que desceu do céu, em nada semelhante àquele que os pais de vocês comeram e, mesmo assim, morreram; quem comer este pão viverá eternamente. " },
    {"versiculo": "59", "texto": "Jesus disse essas coisas quando ensinava na sinagoga de Cafarnaum." },
    {"versiculo": "60", "texto": "Muitos dos seus discípulos, tendo ouvido tais palavras, disseram: — Duro é este discurso; quem pode suportá-lo? " },
    {"versiculo": "61", "texto": "Mas Jesus, sabendo por si mesmo que os seus discípulos murmuravam a respeito do que ele havia falado, disse-lhes: — Isto escandaliza vocês? " },
    {"versiculo": "62", "texto": "Que acontecerá, então, se virem o Filho do Homem subir para o lugar onde primeiro estava? " },
    {"versiculo": "63", "texto": "O Espírito é o que vivifica; a carne para nada aproveita. As palavras que eu lhes tenho falado são espírito e são vida. " },
    {"versiculo": "64", "texto": "Mas há descrentes entre vocês. Ora, Jesus sabia, desde o princípio, quais eram os que não criam e quem iria traí-lo. " },
    {"versiculo": "65", "texto": "E prosseguiu: — Por causa disto é que falei para vocês que ninguém poderá vir a mim, se não lhe for concedido pelo Pai.  " },
    {"versiculo": "66", "texto": "Diante disso, muitos dos seus discípulos o abandonaram e já não andavam com ele. " },
    {"versiculo": "67", "texto": "Então Jesus perguntou aos doze: — Será que vocês também querem se retirar? " },
    {"versiculo": "68", "texto": "Simão Pedro respondeu: — Senhor, para quem iremos? O senhor tem as palavras da vida eterna, " },
    {"versiculo": "69", "texto": "e nós temos crido e conhecido que o senhor é o Santo de Deus." },
]

text_title = 'JOÃO 6:1-69 (NAA)'
write_title(draw, text_title)

pos_top = margin + 150
pos_left = margin
slide = 1

for line in versiculos:
    texto = "    " + line["texto"]
    # Essa funcao corta o texto pelo tamanho de caracteres, é preciso criar outra lógica para cortar por pixels.
    texto = textwrap.fill(texto, 42)
    ver = line["versiculo"]
    line_width, line_height = font_body.getsize(texto)
    text_lines = len(texto.split("\n"))
    text_height = round((line_height * text_lines)) + 40

    print("." + ver + ": L: " + str(text_lines)  + " LH: " + str(line_height) + " TH: " + str(text_height) + " POS:", pos_top + text_height) 

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
    draw.text((pos_left_shadow, pos_top_shadow + 20), ver, font=font_versiculo, fill=(0, 0, 0))
    draw.text((pos_left, pos_top + 20), ver, font=font_versiculo, fill=(210, 186, 81))
    draw.text((pos_left_shadow, pos_top_shadow), texto, font=font_body, fill=(0, 0, 0))
    draw.text((pos_left, pos_top), texto, font=font_body, fill=(255, 255, 255))
    pos_top += text_height   


# img.show()
img.save(output_prefix + str(slide) + ".png")

print('Concluded')
