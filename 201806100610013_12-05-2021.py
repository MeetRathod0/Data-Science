import pandas as pd
import sklearn
import numpy as np
import json

df=pd.read_csv("BigMartSales.csv")

# Find null columns names
null_col=df.columns[df.isnull().any()] # null column contains list of column name

# Set mean value for the null values
df[null_col[0]] = df[null_col[0]].fillna( df[null_col[0]].mean() )

# Set mode value for the null values
df[null_col[1]] = df[null_col[1]].fillna( df[null_col[1]].mode() )

df.to_csv("new.csv")

# find q1
Q1 = np.percentile(df['Item_MRP'], 25, 
                   interpolation = 'midpoint') 
# find q3
Q3 = np.percentile(df['Item_MRP'], 75,
                   interpolation = 'midpoint') 
IQR = Q3 - Q1 

# upper bound
upper =Q3+1.5*IQR

# Lower bound
lower =Q1-1.5*IQR

print("Lower bound: ",lower)
print("Upper bound: ",upper)

"""
try:
    f1=open("NewsDataSet.json")
    jdata=json.load(f1)
    df=pd.DataFrame(jdata)

except Exception as e:
    print(e)
"""
