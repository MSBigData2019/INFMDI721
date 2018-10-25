# coding: utf-8
import requests
import unittest
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

csv = ' John,     47 rue Barrault, 36 ans  '

credits_cards = ' Thanks for paying with 1098-1203-1233-2354    and 2344-1203-3333-2354    '

reg = re.compile(r"(\d{4})-(\d{4})-(\d{4})-(\d{4})")
obfuscation = reg.sub('\g<1>-\g<2>-\g<3>-XXXX',credits_cards)


email = '''
Voici le fichier complété et le calendrier et la liste des adresses des élèves (elles ne seront opérationnelles que la semaine prochaine).








 pierre.arbelet@telECOM-Paristech.fr francois.bLAS@TElecom-parisTECH.fr geoffray.bories@telecom-paristech.fr claire.chazelas@TELECOM-PAristech.fr dutertre@telecom-paristech.fr nde.fOKOU@telecom-paristech.fr wei.he@telecom-paristech.fr anthony.hayot@telecom-paristech.fr frederic.hohner@telecom-paristech.fr yoann.janvier@telecom-paristech.fr mimoune.louarradi@telecom-paristech.fr david.luz@telecom-paristech.fr nicolas.marsallon@telecom-paristech.fr paul.mochkovitch@telecom-paristech.fr martin.prillard@telecom-paristech.fr christian.penon@telecom-paristech.fr gperrin@telecom-paristech.fr anthony.reinette@telecom-paristech.fr florian.riche@telecom-paristech.fr romain.savidan@telecom-paristech.fr yse.wanono@telecom-paristech.fr ismail.arkhouch@telecom-paristech.fr philippe.cayeux@telecom-paristech.fr hicham.hallak@telecom-paristech.fr arthur.dupont@telecom-paristech.fr dabale.kassim@telecom-paristech.fr xavier.lioneton@telecom-paristech.fr sarra.mouas@telecom-paristech.fr jonathan.ohayon@telecom-paristech.fr alix.saas-monier@telecom-paristech.fr thabet.chelligue@telecom-paristech.fr amoussou@telecom-paristech.fr pierre.arbelet@telecom-paristech.fr
'''

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex_email = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
extracts = regex_email.findall(email)


df = pd.Series(extracts).str.upper().str.extract('([A-Z0-9_%+-]+)\.?([A-Z0-9_%+-]*)@([A-Z0-9.-]+)\.([A-Z]{2,4})')


