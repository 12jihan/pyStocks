import requests
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

most_active = requests.get('https://finance.yahoo.com/most-active')

soup = BeautifulSoup(most_active.content, "html.parser")
find_tr = soup.find_all('tr')[1]

symbol = find_tr.contents[0].string

name = find_tr.contents[1].contents[1]

stockPriceInDay = "$ " + find_tr.contents[2].string

stockChange = find_tr.contents[3].string

stockPerChange = find_tr.contents[4].string

stockVol = find_tr.contents[5].string

avgVol = find_tr.contents[6].contents[1]

marketCap = find_tr.contents[7].string

peRatio = find_tr.contents[8].string

print("""
---------------------------------------
++++       Most Active Stocks      ++++
---------------------------------------
|-  {} | {}
|-  Current Price: {}
|-  Stock Change: {}
|-  Percent Change: {}%
|-  {}
|-  {}
""".format(bcolors.BOLD + symbol , name + bcolors.ENDC, stockPriceInDay, stockChange, stockPerChange,"yo", "sup"))