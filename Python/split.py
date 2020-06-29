import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
from sqlalchemy import create_engine

CSV_FILE_PATH = r"C:\Users\Timon\SPI/SuperstoreCleaned.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')
print("CSV size: ", df.shape)

df_1 = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape', nrows = 35000)
print("CSV size: ", df_1.shape)
df_2 = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape', skiprows = range(1, 35001))
print("CSV size: ", df_2.shape)

df_1.to_csv('SuperstoreCleaned_1.csv', index=False)
df_2.to_csv('SuperstoreCleaned_2.csv', index=False)