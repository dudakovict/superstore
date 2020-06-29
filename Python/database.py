import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
import datetime
from sqlalchemy import create_engine

CSV_FILE_PATH = r"C:\Users\Timon\SPI/SuperstoreCleaned_1.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')
print("CSV size: ", df.shape)

user = 'root'
passw = 'timon'
host =  'localhost' 
port = 3306 
database = 'superstore'

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
print(mydb)
connection = mydb.connect()

product_category_ddl = "CREATE TABLE superstore.product_category (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC));"
connection.execute(product_category_ddl)

product_sub_category_ddl = "CREATE TABLE superstore.product_sub_category (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, product_category_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC), CONSTRAINT product_category_id FOREIGN KEY (product_category_fk) REFERENCES superstore.product_category (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(product_sub_category_ddl)

product_ddl = "CREATE TABLE superstore.product (id INT NOT NULL PRIMARY KEY, name VARCHAR(200) NOT NULL, product_sub_category_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC), CONSTRAINT product_sub_category_fk FOREIGN KEY (product_sub_category_fk) REFERENCES superstore.product_sub_category (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(product_ddl)

segment_ddl = "CREATE TABLE superstore.segment (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC));"
connection.execute(segment_ddl)

customer_ddl = "CREATE TABLE superstore.customer (id INT NOT NULL PRIMARY KEY, name VARCHAR(45) NOT NULL, segment_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), CONSTRAINT segment_id FOREIGN KEY (segment_fk) REFERENCES superstore.segment (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(customer_ddl)

market_ddl = "CREATE TABLE superstore.market (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC));"
connection.execute(market_ddl)

region_ddl = "CREATE TABLE superstore.region (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, market_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC), CONSTRAINT market_id FOREIGN KEY (market_fk) REFERENCES superstore.market (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(region_ddl)

country_ddl = "CREATE TABLE superstore.country (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, region_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC), CONSTRAINT region_id FOREIGN KEY (region_fk) REFERENCES superstore.region (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(country_ddl)

state_ddl = "CREATE TABLE superstore.state (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, country_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC), CONSTRAINT country_id FOREIGN KEY (country_fk) REFERENCES superstore.country (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(state_ddl)

city_ddl = "CREATE TABLE superstore.city (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, state_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC), CONSTRAINT state_id FOREIGN KEY (state_fk) REFERENCES superstore.state (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(city_ddl)

ship_mode_ddl = "CREATE TABLE superstore.ship_mode (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC));"
connection.execute(ship_mode_ddl)

order_priority_ddl = "CREATE TABLE superstore.order_priority (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45) NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), UNIQUE INDEX name_UNIQUE (name ASC));"
connection.execute(order_priority_ddl)

order_ddl = "CREATE TABLE superstore.order (id INT NOT NULL PRIMARY KEY, order_date DATE NOT NULL, shipping_cost FLOAT NOT NULL, sales FLOAT NOT NULL, quantity INT NOT NULL, discount FLOAT NOT NULL, profit FLOAT NOT NULL, ship_mode_fk INT NOT NULL, order_priority_fk INT NOT NULL, customer_fk INT NOT NULL, city_fk INT NOT NULL, product_fk INT NOT NULL, UNIQUE INDEX id_UNIQUE (id ASC), INDEX ship_mode_id_idx (ship_mode_fk ASC), INDEX order_priority_id_idx (order_priority_fk ASC), INDEX customer_id_idx (customer_fk ASC), INDEX city_id_idx (city_fk ASC), INDEX product_id_idx (product_fk ASC), CONSTRAINT ship_mode_id FOREIGN KEY (ship_mode_fk) REFERENCES superstore.ship_mode (id) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT order_priority_id FOREIGN KEY (order_priority_fk) REFERENCES superstore.order_priority (id) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT customer_id FOREIGN KEY (customer_fk) REFERENCES superstore.customer (id) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT city_id FOREIGN KEY (city_fk) REFERENCES superstore.city (id) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT product_id FOREIGN KEY (product_fk) REFERENCES superstore.product (id) ON DELETE NO ACTION ON UPDATE CASCADE);"
connection.execute(order_ddl)

product_category_names = df['Category'].unique().tolist()
product_category_data = pd.DataFrame({'id': list(range(1, len(product_category_names) + 1)), 'name': product_category_names})
product_category_data.to_sql(con=mydb, name='product_category', if_exists='append', index=False)

product_sub_category_names = df['Sub-Category'].unique().tolist()
product_category_fk = []
for product_sub_category in product_sub_category_names:
    product_category = df['Category'].loc[df['Sub-Category'] == product_sub_category].unique()
    product_category_fk.append(int(product_category_data['id'].loc[product_category_data['name'].str.contains(product_category[0])]))
product_sub_category_data = pd.DataFrame({'id': list(range(1, len(product_sub_category_names) + 1)), 'name': product_sub_category_names, 'product_category_fk': product_category_fk})
product_sub_category_data.to_sql(con=mydb, name='product_sub_category', if_exists='append', index=False)

product_names = df['Product Name'].unique().tolist()
product_sub_category_fk = []
for product in product_names:
    product_sub_category = df['Sub-Category'].loc[df['Product Name'] == product].unique()
    product_sub_category_fk.append(int(product_sub_category_data['id'].loc[product_sub_category_data['name'].str.contains(product_sub_category[0])]))
product_data = pd.DataFrame({'id': list(range(1, len(product_names) + 1)), 'name': product_names, 'product_sub_category_fk': product_sub_category_fk})
product_data.to_sql(con=mydb, name='product', if_exists='append', index=False)

segment_names = df['Segment'].unique().tolist()
segment_data = pd.DataFrame({'id': list(range(1, len(segment_names) + 1)), 'name': segment_names})
segment_data.to_sql(con=mydb, name='segment', if_exists='append', index=False)

customer_names = df['Customer Name'].unique().tolist()
segment_fk = []
for customer in customer_names:
    segment = df['Segment'].loc[df['Customer Name'] == customer].unique()
    segment_fk.append(int(segment_data['id'].loc[segment_data['name'].str.contains(segment[0])]))
customer_data = pd.DataFrame({'id': list(range(1, len(customer_names) + 1)), 'name': customer_names, 'segment_fk': segment_fk})
customer_data.to_sql(con=mydb, name='customer', if_exists='append', index=False)

market_names = df['Market'].unique().tolist()
market_data = pd.DataFrame({'id': list(range(1, len(market_names) + 1)), 'name': market_names})
market_data.to_sql(con=mydb, name='market', if_exists='append', index=False)

region_names = df['Region'].unique().tolist()
market_fk = []
for region in region_names:
    market = df['Market'].loc[df['Region'] == region].unique()
    market_fk.append(int(market_data['id'].loc[market_data['name'].str.contains(market[0])]))
region_data = pd.DataFrame({'id': list(range(1, len(region_names) + 1)), 'name': region_names, 'market_fk': market_fk})
region_data.to_sql(con=mydb, name='region', if_exists='append', index=False)

country_names = df['Country'].unique().tolist()
region_fk = []
for country in country_names:
    region = df['Region'].loc[df['Country'] == country].unique()
    region_fk.append(int(region_data['id'].loc[region_data['name'] == region[0]]))
country_data = pd.DataFrame({'id': list(range(1, len(country_names) + 1)), 'name': country_names, 'region_fk': region_fk})
country_data.to_sql(con=mydb, name='country', if_exists='append', index=False)

state_names = df['State'].unique().tolist()  
country_fk = []
for state in state_names:
    country = df['Country'].loc[df['State'] == state].unique()
    country_fk.append(int(country_data['id'].loc[country_data['name'] == country[0]]))
state_data = pd.DataFrame({'id': list(range(1, len(state_names) + 1)), 'name': state_names, 'country_fk': country_fk})
state_data.to_sql(con=mydb, name='state', if_exists='append', index=False)

city_names = df['City'].unique().tolist()
state_fk = []
for city in city_names:
    state = df['State'].loc[df['City'] == city].unique()
    state_fk.append(int(state_data['id'].loc[state_data['name'] == state[0]]))
city_data = pd.DataFrame({'id': list(range(1, len(city_names) + 1)), 'name': city_names, 'state_fk': state_fk})
city_data.to_sql(con=mydb, name='city', if_exists='append', index=False)

ship_mode_names = df['Ship Mode'].unique().tolist()
ship_mode_data = pd.DataFrame({'id': list(range(1, len(ship_mode_names) + 1)), 'name': ship_mode_names})
ship_mode_data.to_sql(con=mydb, name='ship_mode', if_exists='append', index=False)

order_priority_names = df['Order Priority'].unique().tolist()
order_priority_data = pd.DataFrame({'id': list(range(1, len(order_priority_names) + 1)), 'name': order_priority_names})
order_priority_data.to_sql(con=mydb, name='order_priority', if_exists='append', index=False)

product_fk, city_fk, ship_mode_fk, customer_fk, order_priority_fk = [], [], [], [], []
for i, row in df.iterrows():
    product = df['Product Name'].iloc[i]
    product_fk.append(int(product_data['id'].loc[product_data['name'] == product]))
    
    city = df['City'].iloc[i]
    city_fk.append(int(city_data['id'].loc[city_data['name'] == city]))
    
    ship_mode = df['Ship Mode'].iloc[i]
    ship_mode_fk.append(int(ship_mode_data['id'].loc[ship_mode_data['name'] == ship_mode]))
    
    customer = df['Customer Name'].iloc[i]
    customer_fk.append(int(customer_data['id'].loc[customer_data['name'] == customer]))
    
    order_priority = df['Order Priority'].iloc[i]
    order_priority_fk.append(int(order_priority_data['id'].loc[order_priority_data['name'] == order_priority]))
    
order_data = pd.DataFrame({'id': list(range(1, len(city_fk) + 1)), 'order_date': df['Order Date'], 'shipping_cost': df['Shipping Cost'], 'sales': df['Sales'], 'quantity': df['Quantity'], 'discount': df['Discount'], 'profit': df['Profit'], 'product_fk': product_fk, 'city_fk': city_fk, 'ship_mode_fk': ship_mode_fk, 'customer_fk': customer_fk, 'order_priority_fk': order_priority_fk})
order_data.to_sql(con=mydb, name='order', if_exists='append', index=False)