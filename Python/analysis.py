import pymysql
import pandas as pd
import numpy as np
import json
import requests
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
CSV_FILE_PATH = r"C:\Users\Timon\SPI/Superstore.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',', encoding= 'unicode_escape')

print(df.head())
print("CSV size: ", df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df.nunique())
print(df["Ship Mode"].unique().tolist())
print(df["Category"].unique().tolist())
print(df["Order Priority"].unique().tolist())
print(df["Segment"].unique().tolist())
print(df["Market"].unique().tolist())
print(df["Ship Mode"].value_counts())
print(df["Category"].value_counts())
print(df["Order Priority"].value_counts())
print(df["Segment"].value_counts())
print(df["Market"].value_counts())
print(df.loc[df["Profit"].idxmin()])
print(df.loc[df["Profit"].idxmax()])

office_supplies_profits = []
technology_profits = []
furniture_profits = []
for row, i in df.iterrows():
    if i['Category'] == 'Office Supplies':
        office_supplies_profits.append(i['Profit'])
    elif i['Category'] == 'Technology':
        technology_profits.append(i['Profit'])
    else:
        furniture_profits.append(i['Profit'])
profits = [round(sum(office_supplies_profits), 2), round(sum(technology_profits), 2), round(sum(furniture_profits), 2)]
frequencies = [len(office_supplies_profits), len(technology_profits), len(furniture_profits)]
print(profits)
print(frequencies)
labels = 'Office Supplies', 'Technology', 'Furniture'
sizes_profits = [round(100 * float(profits[0])/float(sum(profits)), 2),
        round(100 * float(profits[1])/float(sum(profits)), 2),
        round(100 * float(profits[2])/float(sum(profits)), 2)]
sizes_frequencies = [round(100 * float(frequencies[0])/float(sum(frequencies)), 2),
        round(100 * float(frequencies[1])/float(sum(frequencies)), 2),
        round(100 * float(frequencies[2])/float(sum(frequencies)), 2)]
explode_profits = [0, .1, 0]
explode_frequencies = [.1, 0, 0]
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(sizes_profits, explode = explode_profits, labels = labels, autopct='%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')
ax2.pie(sizes_frequencies, explode = explode_frequencies, labels = labels, autopct='%1.1f%%', shadow = True, startangle = 90)
ax2.axis('equal')
plt.title('Profits - Frequencies')
plt.show()

