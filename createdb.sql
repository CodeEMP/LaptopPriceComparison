--creates apidata table, where the api data is stored 

CREATE TABLE apidata (
  id SERIAL NOT NULL PRIMARY KEY,
  sku varchar NOT NULL,
  productname varchar NOT NULL,
  best_selling_rank integer,
  manufacturer varchar,
  sale_price decimal,    
  short_description varchar,
  image_url varchar,
  regular_price decimal,
  onsale boolean, 
  as_of timestamp
);

--sql to get data from apidata, replace 6190769, probably have to use %s to replace python variable
SELECT * FROM apidata
WHERE (sku, as_of) IN (SELECT sku, MAX(as_of) FROM apidata GROUP BY sku) AND sku LIKE '6190769';
