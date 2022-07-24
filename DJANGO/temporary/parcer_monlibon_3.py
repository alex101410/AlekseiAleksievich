import requests
from bs4 import BeautifulSoup as BS
import csv
import time

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


def get_html(URL):
    r = requests.get(URL, headers=HEADERS)
    return r

def get_pages_count(r):
    soup = BS(r.text, 'html.parser')
    return soup

def get_content(soup):
    data = []
    i = 0
    for k in soup:

        brend = soup.findAll('a', class_='fancy_inline droppeda danger-hover-link brand-search')[i].text.strip()
        article = soup.findAll('a', style="font-size: 14px")[i].text.strip()
        quantity = soup.findAll('div', class_='col-4 col-sm-2 col-lg-1 text-center m-auto')[i].text.strip()
        cost = soup.findAll('span', class_='old_PriceLevel')[i].text.strip()
        if article != '':
            data.append({
                    'brend': brend,
                    'article': article,
                    'quantity': quantity,
                    'cost': cost,
            })
        i+=1
    return data

def save_file(data, FILE):
    with open(FILE, 'w',  encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Бренд', 'Артикул', 'Количество', 'Цена'])
        for i in data:
            writer.writerow([i['brend'], i['article'], i['quantity'], i['cost']])

def parse():
#    parts = ['k2056c3', 'k1956']
    parts = tuple(input("введите артикул\n"))
    for part in parts:


        URL = f'https://www.ml-auto.by/search/number/?article={part}&brand=FENOX&ajax=true'
        print(URL)
        r = get_html(URL)

        soup = get_pages_count(r)
        data = get_content(soup)
        data.extend(get_content(soup))
        time.sleep(1)
        FILE = 'Parse_MONLIBON' + '.csv'   
        save_file(data, FILE)
parse()