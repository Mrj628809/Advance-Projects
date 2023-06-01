'''
Parse Alphavantage API

Author: Matthew Judson(Mrj628809@gmail.com)
Last Revised: 2 / 3 / 2023
'''
import requests
import json
import statistics
import matplotlib.pyplot as plt

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API KEY}'
r = requests.get(url)
result = json.loads(r.text)

ticker = result["Meta Data"]["2. Symbol"]
date = result["Meta Data"]["3. Last Refreshed"][0:10]
high_num = []
low_num = []
close_num = []

for values in result["Time Series (5min)"]:
    ikeys = result["Time Series (5min)"][values]
    high_num.append(float(ikeys['2. high']))
    low_num.append(float(ikeys['3. low']))
    close_num.append(float(ikeys['4. close']))

print(f'Date:  {date}')
print(f'High: {max(high_num)}')
print(f'Low: {min(low_num)}')
print(f'Standard Deviation:  {statistics.stdev(close_num)}')

plt.plot(close_num)
plt.savefig(f'{ticker}.png')

