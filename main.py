import requests
from bs4 import BeautifulSoup

URL = "https://auto.drom.ru/mercedes-benz/new/all/"
HEADERS = ...


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='css-1dk6v6x')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='css-17lk78h e3f4v4l2').get_text(strip=True),
            # 'link': item.find('a', class_='css-1dk6v6x ewrty960').get('href')
            'ruble_price': item.find('span', class_='css-107ouu3 e162wx9x0').get_text()
        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
