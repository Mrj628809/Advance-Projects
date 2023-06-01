'''
solution_1.5.py - - Writing rows with selected columns

Author: Matthew Judson(Mrj628809@gmail.com)
Last Revised: 1 / 23 / 2023
'''

import csv

filename = 'weather_newyork_tiny.csv'

fh = open(filename)
reader = csv.reader(fh)

wfh = open('weather_newyork_narrow.csv', 'w', newline='')
writer = csv.writer(wfh)

for row in reader:
    date,mean_temp,max_dewpoint,mean_dewpoint,min_dewpoint,max_humidity,mean_humidity,min_humidity,max_sealevel,mean_sealevel,min_sealevel,max_visibility,mean_visibility,min_visibility,max_windspeed,mean_windspeed,max_gustspeed,precip,cloudcover,events,wind_dir_deg = row
    writer.writerow([date, mean_temp, precip, events])

wfh.close()
