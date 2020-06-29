import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
import unidecode
import datetime
from sqlalchemy import create_engine

CSV_FILE_PATH = r"C:\Users\Timon\SPI/SuperstoreCleaned_2.csv"
df_csv = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')
print("CSV size: ", df_csv.shape)

user = 'root'
passw = 'timon'
host =  'localhost' 
port = 3306 
database = 'superstore'

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
print(mydb)
connection = mydb.connect()
df_db = pd.read_sql('SELECT order_date FROM superstore.order', con = mydb)

dates_db = []
for date in df_db['order_date']:
    dates_db.append(str(date))

dates_csv = df_csv['Order Date']
dates_db = pd.Series(dates_db, name = 'Order Date')
dates = dates_db.append(dates_csv, ignore_index = True)
dates = dates.tolist()

df_db = pd.read_sql('SELECT order_date FROM superstore.order', con = mydb)
dates_db = []
for date in df_db['order_date']:
    dates_db.append(str(date))
dates_csv = df_csv['Order Date']
dates_db = pd.Series(dates_db, name = 'Order Date')
dates = dates_db.append(dates_csv, ignore_index = True)
dates = dates.unique().tolist()
days, months, years = [], [], []
for date in dates:
    splitted = []
    splitted = date.split('-')
    years.append(splitted[0])
    if (splitted[1].startswith('0')):
        month = splitted[1].split('0')[1]
        months.append(month)
    else:
        months.append(splitted[1])
    if (splitted[2].startswith('0')):
        day = splitted[2].split('0')[1]
        days.append(day)
    else:
        days.append(splitted[2])
dim_date_data = pd.DataFrame({'date_tk':list(range(1,len(dates)+1)), 'date': dates, 'year':years, 'month':months, 'day': days})
dim_date_data.to_sql(con=mydb, name='dim_date', if_exists='append', index=False)