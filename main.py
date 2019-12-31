import requests
from bs4 import BeautifulSoup

most_active = requests.get('https://finance.yahoo.com/most-active')

# print(getpage.content)
soup = BeautifulSoup(most_active.content, "html.parser")


item_num = 0
for item in soup.find_all('tr')[1].contents:
    item_num += 1
    print(item_num)
    print('````')
    print(item.contents)
    print('--------------------------------------------------------------------------')

# item_num = 0
# for item in soup.find_all('tr'):
#     item_num += 1
#     print(item_num)
#     print('`````````````````````````````````````````````````')
#     # print(item.find_all('a'))
#     print(item.find_all('td'))
#     print   ("----------------------------------------------------------------------------------------------------------------------------------------------------")


# print(soup.find_all('tr')[1])