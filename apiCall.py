import json
import requests
import psycopg2

r = requests.get('https://api.bestbuy.com/v1/products(bestSellingRank>0&(categoryPath.id=abcat0502000))?apiKey=APIKEY&sort=bestSellingRank.asc&show=bestSellingRank,manufacturer,name,salePrice,image,regularPrice,onSale,shortDescription,sku&pageSize=25&format=json')
data = r.json()

for a in range (0,26):
    data['products'][a]['name']
    data['products'][a]['manufacturer']
    data['products'][a]['sku']
    data['products'][a]['salePrice']