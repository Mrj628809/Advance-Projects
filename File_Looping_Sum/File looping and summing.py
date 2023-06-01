'''
solution_1.1.py - - File looping summing

Author: Matthew Judson(Mrj628809@gmail.com)
Last Revised: 1 / 19 / 2023
'''

filename = 'ad_buys.csv'
fh = open(filename)
headers = next(fh)

list_num = []

for line in fh:
    line = line.split(',')
    if line[1] == '1':
        print(line[4])
        list_num.append(float(line[4]))

fh.close()

print(f'sum: {round(sum(list_num), 3)}')
