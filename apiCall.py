import json
import requests
import psycopg2
import time
import os

apikey = os.environ.get('API_KEY')

r = requests.get('https://api.bestbuy.com/v1/products(bestSellingRank>0&(categoryPath.id=abcat0502000))?apiKey='+apikey+'&sort=bestSellingRank.asc&show=bestSellingRank,manufacturer,name,salePrice,image,regularPrice,onSale,shortDescription,sku&pageSize=50&format=json')
data = r.json()

conn = psycopg2.connect("host=ec2-54-83-204-6.compute-1.amazonaws.com dbname=dcnhjrhmqkb069 user=ukzppuglreogfo password=017f117fb05419ba5c631061538bcf6f6220091f5b98fdbb4573882ab7fd65e2")
cur = conn.cursor()

for a in range (0,50):
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
    %s, %s, %s, %s, %s, %s);
    """,
    (sku,prodName,bestSellingRank,manufacturer,salePrice,shortDescription,image,regularPrice,onSale, currTime))
    conn.commit()

cur.close()
conn.close()
