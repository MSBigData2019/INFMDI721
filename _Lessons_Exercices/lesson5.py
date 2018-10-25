# -*- coding: utf8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import re

# wide to long
releves = [
         ['lundi','temperature',28]
         ,['lundi','ensoleillement',4]
         ,['lundi','pollution',5]
         ,['lundi','pluie',100]
         ,['mardi','temperature',28]
         ,['mardi','ensoleillement',4]
         ,['mardi','pollution',5]
         ,['mardi','pluie',100]
         ,['mercredi','temperature',28]
         ,['mercredi','ensoleillement',4]
         ,['mercredi','pollution',5]
         ,['mercredi','pluie',100]
         ,['jeudi','temperature',28]
         ,['jeudi','ensoleillement',4]
         ,['jeudi','pollution',5]
         ,['jeudi','pluie',100]
         ,['vendredi','temperature',28]
         ,['vendredi','ensoleillement',4]
         ,['vendredi','pollution',5]
         ,['vendredi','pluie',100]
         ]

df = pd.DataFrame(releves, columns=['day','metric','value'])
df_wide = df.pivot(index='day',columns='metric',values='value')


cameras = pd.read_csv('Camera.csv',sep=';',skiprows=[1])

pd.melt(cameras,['Model'],cameras.columns[1:])
cameras[['Brand','Model_without_brand']] = cameras['Model'].str.extract(r'(\w+) ([\w\s]+)')
mean_price = cameras.groupby('Brand')['Price'].mean()
cameras.groupby(['Brand','Release date'])['Price'].mean()
cameras.groupby('Brand').agg({'Price':np.mean ,'Max resolution':np.max})
cameras.merge(pd.DataFrame(mean_price),left_on='Brand', right_index=True)


def top_n(df, n=5, column="Max resolution"):
    return df.sort_values(column,ascending=False)[:n]

