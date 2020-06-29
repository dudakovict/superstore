import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
from sqlalchemy import create_engine

user = 'root'
passw = 'timon'
host =  'localhost' 
port = 3306 
database = 'superstore'

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
print(mydb)
connection = mydb.connect()

product_ddl = 'CREATE TABLE superstore.dim_product (product_tk BIGINT PRIMARY KEY, version INT, date_from DATETIME, date_to DATETIME, product_id INT, product_name VARCHAR(200), product_sub_category VARCHAR(45), product_category VARCHAR(45))';
connection.execute(product_ddl)

location_ddl = 'CREATE TABLE superstore.dim_location (city_tk BIGINT PRIMARY KEY, version INT, date_from DATETIME, date_to DATETIME, city_id INT, city_name VARCHAR(45), state_name VARCHAR(45), country_name VARCHAR(45), region_name VARCHAR(45), market_name VARCHAR(45))';
connection.execute(location_ddl)

customer_ddl = 'CREATE TABLE superstore.dim_customer (customer_tk BIGINT PRIMARY KEY, version INT, date_from DATETIME, date_to DATETIME, customer_id INT, customer_name VARCHAR(45), segment VARCHAR(45))';
connection.execute(customer_ddl)

date_ddl = 'CREATE TABLE superstore.dim_date (date_tk INT AUTO_INCREMENT PRIMARY KEY, date DATE, year INT, month INT, day INT, UNIQUE INDEX date_tk_UNIQUE (date_tk ASC))';
connection.execute(date_ddl)

order_ddl = 'CREATE TABLE superstore.dim_order (order_tk INT AUTO_INCREMENT PRIMARY KEY, product_id BIGINT NOT NULL, location_id BIGINT NOT NULL, customer_id BIGINT NOT NULL, date_id INT NOT NULL, ship_mode VARCHAR(45) NOT NULL, order_priority VARCHAR(45) NOT NULL, shipping_cost FLOAT NOT NULL, sales FLOAT NOT NULL, quantity INT NOT NULL, discount FLOAT NOT NULL, profit FLOAT NOT NULL, CONSTRAINT product_tk FOREIGN KEY (product_id) REFERENCES superstore.dim_product (product_tk) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT location_tk FOREIGN KEY (location_id) REFERENCES superstore.dim_location (city_tk) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT customer_tk FOREIGN KEY (customer_id) REFERENCES superstore.dim_customer (customer_tk) ON DELETE NO ACTION ON UPDATE CASCADE, CONSTRAINT date_tk FOREIGN KEY (date_id) REFERENCES superstore.dim_date (date_tk) ON DELETE NO ACTION ON UPDATE CASCADE, UNIQUE INDEX order_tk_UNIQUE (order_tk ASC))';
connection.execute(order_ddl)