import json
import pandas as pd
import numpy as np
import datetime as dt
#f1 = open("MEETFILE1.json")
#jdata = json.load(f1)

#df = pd.DataFrame(jdata)
#df.to_csv("jsonOpNEW.csv")

# Date operation 
df = pd.read_csv("SalesJan2009.csv")

df['Transaction_date'] = pd.to_datetime(df['Transaction_date'])

# print(df['Transaction_date'].dt.year) # print only  year
print(df.Price)

include = df[df['Transaction_date'].dt.year == 2009]

include = df[ (df['Transaction_date'].dt.year == 2009) & (df['Price'] == 3600) ]

print(include)