# Llamallamallama

Camelcamelcamel clone for Best Buy laptops

An app that pulls and stores price data from Best Buy’s API for the 50 most popular laptops. Shows current price and price history. 



## Team
Cody, Chih-Ming, Jim 

## MVP (Minimum Viable Product) 
[x] Pull data from Best Buy API’s 50 most popular laptops and store in a database

[x] Allow search by SKU (stock keeping unit, a unique id for every product) and return price data

[x] Show price history of item

## Stretch Goals
[ ] Search by keyword and SKU

[x] Show listing of items in database

[ ] Create a graph of price history 

[ ] Add page of most popular items

[ ] Add page of biggest price reductions from regular price 

[ ] If search item does not exist in database, do one off API call

[ ] Create user accounts

[ ] Price drop alert, user sets up price drop notification, if price drops below set price, email is sent 

## Experience
-Initially wanted to do app that pulled prices from Amazon API and Bestbuy API and compare them (since Best Buy will price match Amazon), but getting Amazon API key was time consuming since you had to go through an approval process. Best Buy’s API key approval process was shorter and was able to get key, so decided to work with only Best Buy 

-Decided everyone would work on part most familiar with, Chih-Ming did the front end, Cody did the back end and deployment, and Jim did the database and SQL queries. Since there was very little overlap, this contributed to very few merge issues. 

-Decided to populate database with 25 most popular laptops and fortunately API had ability to rank products by popularity. Team was confused initially as setting criteria to laptops only and item ranking less than 25 would not return anything. Eventually realized that item ranking was for all items and API was returning top 25 selling laptops, just price ranking would not be sequential since ranking was for all items

-Later changed API call to top 50 laptops as laptops would often drop out of top 25 and we wanted to be able to show a price history. 

-Ran into issues pushing local database to Heroku, Jim tried saving database out to Amazon S3 but could not find Heroku DB URL only URI, Cody was able to push using Heroku command lines 

-Had issues linking to Heroku database, getting Heroku scheduler linking to database 

-Confusion over merging into master, sometimes accidentally pushing to master, some users had settings with commits automatically merging into master 
