import json
import requests

r = requests.get('https://api.bestbuy.com/v1/products(bestSellingRank>=0&(categoryPath.id=abcat0502000))?apiKey=eGImbuo7MJWkAS1UEcTFn7cj&sort=bestSellingRank.asc&show=bestSellingRank,manufacturer,salePrice,shortDescription,sku&format=json')
r.json()
json.loads(r)
json.dumps(r)