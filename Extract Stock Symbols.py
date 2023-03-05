"""
Extract all mentions of stock symbols and price changes from a news article

 Author: Matthew Judson (mrj628809@gmail.com)
 Last Revised: 2/11/2023
"""

import re

fh = open('market_discussion.txt')
news = fh.read()
nlist = {}

for tic in sorted(re.findall(r'[A-Z]+, [-+]\d+.\d+',news)):
    print(tic)

print('========')

def comtup(tup):
    return float(tup[1])

tlist = re.findall(r'([A-Z]+,) ([-+]\d+.\d+)', news)
sortval = dict(sorted(tlist, key=comtup, reverse=True))

for key in sortval:
    val = sortval[key]
    sortval[key] = float(val)

for key, value in sortval.items():
    print(key,value)





