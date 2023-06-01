"""
 solution_6.4.py -- Python for Alpha Vantage

 Author: Matthew Judson (mrj628809@gmail.com)
 Last Revised: 2/27/2023
"""

import requests

class Prices:

    def __init__(self, symbol, interval, apikey):

        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={apikey}'
        r = requests.get(url)


        self.data = r.json()
        self.symbol = self.data['Meta Data']['2. Symbol']
        self.interval = self.data['Meta Data']['4. Interval']
        self.last_refreshed = self.data['Meta Data']['3. Last Refreshed']

    def get_close(self):
        clist = []
        for i in self.data['Time Series (15min)']:
            clist.append(self.data['Time Series (15min)'][i]['4. close'])
        return clist

    def last(self,vitem):
        return self.get_close()[0]

    def series(self,vlist):
        return self.get_close()

ibm = Prices(symbol='IBM', interval='15min', apikey='1AWYRGZ8WNZCJEXD')

print(ibm.symbol)           # IBM

print(ibm.interval)         # 15min

print(ibm.last_refreshed)   # 2020-10-19 20:00:00

print(ibm.last('close'))    # 121.8900

print(ibm.series('close'))  # ["121.8900", "121.8000", "121.9300" ...]




