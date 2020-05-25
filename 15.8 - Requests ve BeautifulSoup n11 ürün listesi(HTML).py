from bs4 import BeautifulSoup
import requests

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

count = soup.find('div', {'class': 'listView'}).find('ul').find('li').find('div').get('data-searchcount')
count = int(count)

page = 1
while page < count/28:

    url = f'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg={page}'

    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')

    list = soup.find_all('li',{'class':'column'})

    page = page + 1
    print(url)

    for li in list:
        name = li.div.a.h3.text.strip()
        price = li.find('div',{'class':'proDetail'}).find_all('a')[0].text.strip().strip('TL').strip()
        print(f'Ürün : {name.ljust(75)} Fiyat: {price} ₺' )
