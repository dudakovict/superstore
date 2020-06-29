import csv
import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
from sqlalchemy import create_engine

txt_file = 'SuperstoreReduced.txt'
CSV_FILE_PATH = r"C:\Users\Timon\SPI/SuperstoreCleaned.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')

del df['Ship Mode']
del df['Customer Name']
del df['Segment']
del df['City']
del df['State']
del df['Country']
del df['Market']
del df['Product Name']
del df['Region']
del df['Sales']
del df['Discount']
del df['Shipping Cost']
del df['Order Priority']

df.to_csv('SuperstoreReduced.csv', index=False)
CSV_FILE_PATH = r"C:\Users\Timon\SPI/ApacheFlink.csv"
with open(txt_file, "w") as my_output_file:
    with open(CSV_FILE_PATH, "r") as my_input_file:
        [ my_output_file.write(",".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()