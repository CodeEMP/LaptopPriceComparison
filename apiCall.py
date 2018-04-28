import json
import requests

r = requests.get('https://api.bestbuy.com/v1/products(bestSellingRank>0&(categoryPath.id=abcat0502000))?apiKey=APIKEY&sort=bestSellingRank.asc&show=bestSellingRank,manufacturer,salePrice,shortDescription,sku,name&pageSize=25&format=json')
data = r.json()

for a in range (0,26):
    data['products'][a]['name']
    data['products'][a]['manufacturer']
    data['products'][a]['sku']
    data['products'][a]['salePrice']