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

