import requests
from bs4 import BeautifulSoup as BS

from django.core.management.base import BaseCommand
from aparser.models import Product

class MonlibonParser:



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
  

    def get_html(URL, HEADERS):
        r = requests.get(url=URL, headers=HEADERS)
        return r.text

    def get_content(r):
        soup = BS(r.text, 'html.parser')
        return soup

    def get_product(soup):
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

        p = Product(catalog).save()
        print(f'product {p}')
        return catalog


class Command(BaseCommand):
    help = 'Парсинг Momlibon'
    def handle(self, *args, **options):
        p = MonlibonParser()

#         URL = f'https://www.ml-auto.by/search/number/?article=k1956&brand=FENOX&ajax=true'
#         r = get_html(URL)
#         soup = get_pages_count(r)
#         data = get_content(soup)
# #        data.extend(get_content(soup))
#         time.sleep(1)


