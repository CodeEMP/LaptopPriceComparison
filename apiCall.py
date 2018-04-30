import json
import requests
import psycopg2
import time

r = requests.get('https://api.bestbuy.com/v1/products(bestSellingRank>0&(categoryPath.id=abcat0502000))?apiKey=KEY&sort=bestSellingRank.asc&show=bestSellingRank,manufacturer,name,salePrice,image,regularPrice,onSale,shortDescription,sku&pageSize=25&format=json')
data = r.json()

conn = psycopg2.connect("dbname=apidb user=postgres")
cur = conn.cursor()

for a in range (0,25):
    sku = data['products'][a]['sku']
    prodName = data['products'][a]['name']
    bestSellingRank = data['products'][a]['bestSellingRank'] 
    manufacturer = data['products'][a]['manufacturer']
    salePrice = data['products'][a]['salePrice']
    shortDescription = data['products'][a]['shortDescription']
    image = data['products'][a]['image']
    regularPrice = data['products'][a]['regularPrice']
    onSale = data['products'][a]['onSale']
    currTime = time.strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("""
    INSERT INTO apidata 
    VALUES (DEFAULT, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, '2017-07-23');
    """,
    (sku,prodName,bestSellingRank,manufacturer,salePrice,shortDescription,image,regularPrice,onSale))
    conn.commit()

cur.close()
conn.close()
