import requests as RQ
from bs4 import BeautifulSoup as BS
import json

sku = input("Enter product sku: ")
URL = "https://courtsidenc.co/products/" + sku
page = RQ.get(URL)
pageParsed = BS(page.content, 'html.parser')
json_element = json.loads((str((pageParsed.find(id='ProductJson-product-template')).getText())).strip())
productTitle = json_element['title']
vars = {}
for variant in json_element['variants']:
    vars[variant['title']] = {'price':variant['price']}
print(str(vars))