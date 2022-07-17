#!/usr/bin/env python3
from bible import Bible
from generator import Generator

bible = Bible('NAA') # [ARA, NAA, NVI]
gen = Generator(bible)
gen.debug = True
gen.template = 'bible-classic' # bible-classic, green-sky
gen.generate("Lucas 18:31-34")
gen.generate("Lucas 13:31-35")
gen.generate("Filipenses 2:5-11")
gen.generate("Salmos 84:5")
bible.set_version('NVI')
gen.generate("Salmos 84:5")
gen.save('output/Pregacao-07-17')

print('Concluded')
