import requests
from bs4 import BeautifulSoup as BS
# import csv
# import time

#code = input(f'введите артикул \n')
#data =[]
URL = 'https://auto1.by/details?id=454857'
HEADERS = {
    'Accept': '*/*',
    'Host': 'auto1.by',
    'Referer': 'https://auto1.by/search?pattern=k2056c3',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
print(URL)
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    print(r.text)
    return r
def parse():
    html = get_html(URL)
    print(html.status_code, 'WTF')
#     soup = BS(r.text, 'html.parser')
#     print(soup)
#     ID = soup.find('a', class_='paddingStyle').text.strip
#     data.append({'ID':ID})
#     return data
# print(data)

#parce()