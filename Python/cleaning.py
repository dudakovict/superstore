import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
import unidecode
import datetime
from sqlalchemy import create_engine

CSV_FILE_PATH = r"C:\Users\Timon\SPI/Superstore.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')
print("CSV size: ", df.shape)

import unidecode

country_names = df["Country"].tolist()
state_names = df["State"].tolist()
city_names = df["City"].tolist()
cleaned = []

for country in country_names:
    cleaned.append(unidecode.unidecode(country))
    
cleaned = pd.Series(cleaned, name = "Country")
df.update(cleaned)

cleaned = []

for state in state_names:
    cleaned.append(unidecode.unidecode(state))

cleaned = pd.Series(cleaned, name = "State")
df.update(cleaned)

cleaned = []

for city in city_names:
    cleaned.append(unidecode.unidecode(city))
    
cleaned = pd.Series(cleaned, name = "City")
df.update(cleaned)

import datetime

order_dates = df["Order Date"].tolist()
order_days, order_months, order_years, cleaned = [], [], [], []
for date in order_dates:
    splitted = []
    if ('/' in date):
        splitted = date.split('/')
    else:
        splitted = date.split('-')
    order_days.append(splitted[0])
    order_months.append(splitted[1])
    order_years.append(splitted[2])

for i in range(0, len(order_days)):
    cleaned.append(order_years[i] + '-' + order_months[i] + '-' + order_days[i])
    
cleaned = pd.Series(cleaned, name = "Order Date")
df.update(cleaned)

del df["Order ID"]
del df["Ship Date"]
del df["Product ID"]
del df["Customer ID"]
del df["Postal Code"]
del df["Row ID"]

df.to_csv('SuperstoreCleaned.csv', index=False)