import requests
from bs4 import BeautifulSoup

most_active = requests.get('https://finance.yahoo.com/most-active')

soup = BeautifulSoup(most_active.content, "html.parser")

symbol = soup.find_all('tr')[1].contents[0].string

name = soup.find_all('tr')[1].contents[1].contents[1]

stockPriceInDay = soup.find_all('tr')[1].contents[2].string

stockChange = soup.find_all('tr')[1].contents[3].string

stockPerChange = soup.find_all('tr')[1].contents[4].string

stockVol = soup.find_all('tr')[1].contents[5].string

avgVol = soup.find_all('tr')[1].contents[6].contents[1]

marketCap = soup.find_all('tr')[1].contents[7].string

peRatio = soup.find_all('tr')[1].contents[8].string

print("""
---------------------------------------
++++       Most Active Stocks      ++++
---------------------------------------
|+ one
|+ two
|+ three
""")