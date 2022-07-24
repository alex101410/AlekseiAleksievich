import requests
from bs4 import BeautifulSoup as BS
#import csv
#import time
#import fake_useragent

#user = fake_useragent.UserAgent().random
#header = {'user-agent': user}

HEADERS = {
    'Host': 'www.ml-auto.by',
    'Referer': 'https://www.ml-auto.by/search/preload/?article=K2056c3',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


url = 'https://www.ml-auto.by/search/number/?article=K2056C3&brand=FENOX&ajax=true'
r = requests.get(url, headers=HEADERS)
soup = BS(r.text, 'html.parser')


catalog = []
# for item in items:
#     item = str(item)


catalog.append({
    'brend': soup.find('a', class_='fancy_inline droppeda danger-hover-link brand-search').text.strip(),

    'article': soup.find('a', style="font-size: 14px").text.strip(),

    'description': soup.find('p', class_='mb-2').text.strip(),

    'quantity': soup.find('div', class_='col-4 col-sm-2 col-lg-1 text-center m-auto').text.strip(),

    'cost': soup.find('span', class_='old_PriceLevel').text.strip()

})

print(catalog)
