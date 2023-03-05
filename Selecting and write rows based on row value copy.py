'''
solution_1.6.py - - Selecting and write rows based on row value

Author: Matthew Judson(Mrj628809@gmail.com)
Last Revised: 1 / 24 / 2023
'''

import csv

filename = 'revenue.csv'

fh = open(filename)
reader = csv.reader(fh)

wfh = open('revenue_ny.csv', 'w', newline='')
writer = csv.writer(wfh)
writer.writerow(['company', 'state', 'price'])

for row in reader:
    company, state, price = row

    if state == 'NY':
        writer.writerow([company, state, price])

wfh.close()
