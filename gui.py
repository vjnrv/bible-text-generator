#!/usr/bin/env python3
from bible import Bible
from generator import Generator
import PySimpleGUI as sg
import sys

versions = ['NAA', 'ARA', 'NVI']
themes = ['Clássico', 'Céu estrelado']
layout = [
    [sg.Text("Versão da Bíblia")],
    [sg.Combo(versions, default_value='NAA', key='version')],
    [sg.Text("Tema")],
    [sg.Combo(themes, default_value='Clássico', key='theme')],
    [sg.Text("Qual o texto? Insira no formato: Lucas 17.11-19")],
    [sg.Input(key='texto')],
    [sg.Button('Gerar Slides')] ]
window = sg.Window('Bible Text Generator', layout)
event, values = window.read()

if not values['texto']:
    sys.exit()

theme = 'green-sky' if values['theme'] == 'Céu estrelado' else 'bible-classic'
output_dir = 'output/%s' % (values['texto'].replace(' ', '').replace(':', '_'))
bible = Bible(values['version']) # ARA, NAA
gen = Generator(bible)
gen.debug = True
gen.template = theme # bible-classic, green-sky
gen.generate(values['texto'])
gen.save(output_dir)
gen.opendir(output_dir)
window.close()
sys.exit()

# BUILD: https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen/59558614#59558614
# - pyinstaller --hiddenimport win32timezone -F gui.py
# - pyinstaller --onefile --windowed gui.py
