import requests
from bs4 import BeautifulSoup as BS


def get_html():
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
    print(r.text)
    return(r.text)
get_html()
    
