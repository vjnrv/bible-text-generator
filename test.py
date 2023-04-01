#!/usr/bin/env python3
from bible import Bible
from generator import Generator

bible = Bible('NAA') # [ARA, NAA, NVI]
gen = Generator(bible)
gen.debug = True
gen.template = 'bible-classic' # bible-classic, green-sky
gen.generate("Lucas 19:45-48")
gen.generate("Lucas 20:1-18")
# bible.set_version('NVI')
gen.save('output/Pregacao-08-27')

print('Concluded')
