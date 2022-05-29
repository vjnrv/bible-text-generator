#!/usr/bin/env python3
from bible import Bible
from generator import Generator

bible = Bible('ARA') # ARA, NAA
gen = Generator(bible)
gen.debug = True
gen.template = 'green-sky' # bible-classic, green-sky
gen.generate("1 Coríntios 9.25-27")
gen.generate("João 12.20-28")
gen.generate("Atos 13.25")
gen.generate("2 Timóteo 4.6-8")
gen.generate("Atos 20:24")
gen.save('output/Pregacao05-29')
print('Concluded')
