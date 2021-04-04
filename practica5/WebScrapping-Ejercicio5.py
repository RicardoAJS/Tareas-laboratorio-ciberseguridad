import requests

from bs4 import BeautifulSoup

#Ricardo Adhiel Jacobo Sanjuan

url = 'https://gamamusic.com/venta-instrumentos-musicales/baterias/baterias-acusticas'

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

prod = soup.find_all('p', class_='product-name color-purple-dark')

productos = list()

for i in prod :
    productos.append(i.text)
print(productos)
