#!/usr/bin/env python3
from bible import Bible
from generator import Generator
from theme import Theme

bible = Bible('NAA') # [ARA, NAA, NVI]
theme = Theme('classic')
gen = Generator(bible, theme)
gen.debug = True
gen.generate("Lucas 18:35-43")
# bible.set_version('NVI')
gen.save('output/Testes-Novo-Tema')

print('Concluded')
