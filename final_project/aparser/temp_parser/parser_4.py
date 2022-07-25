import requests
from bs4 import BeautifulSoup as BS

def parse():
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
    URL = f'https://www.ml-auto.by/search/number/?article=K2056c3&brand=FENOX&ajax=true'



    r = requests.get(url=URL, headers=HEADERS)

    soup = BS(r.text, 'html.parser')



    brends = soup.findAll('a', class_='fancy_inline droppeda danger-hover-link brand-search')
    articles = soup.findAll('a', style="font-size: 14px")
    quantitys = soup.findAll('div', class_='col-4 col-sm-2 col-lg-1 text-center m-auto')
    costs = soup.findAll('span', class_='old_PriceLevel')

    catalog = []
    i = 0
    for articles[i] in articles:
        brend = brends[i].text.strip()
        article = articles[i].text.strip()
        quantity = quantitys[i].text.strip()
        cost = costs[i].text.strip()
        if article != '':
            catalog.append({'brend':brend,'article':article, 'quantity':quantity, 'cost':cost})


    print(catalog)
    return catalog
