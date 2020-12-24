# data processing 

# case 1

# -*- coding: utf-8 -*-
"""
ts.csv is as below, suppose this is a purchase order

food,ounces,animal
bacon,4,pig
pulled pork,3,pig
bacon,NaN,pig
Pastrami,6,cow
corned beef,7.5,cow
Bacon,8,pig
pastrami,-3,cow
honey ham,5,pig
nova lox,6,salmon
corned beef,NaN,cow

"""
import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
df = DataFrame(pd.read_csv('D:/Download/Chrome/ts.csv'))

'''
here is my thinking about data clean
1. food column to low letters
2. the same name to use the mean of the values
3. use absolute value to the numbers
'''
df['food'] = df['food'].str.lower() # this line complete the first goal

nanfoodname = df['food'][df['ounces'].isnull()] # return a Series which include nan in ounces
nanfoodname = nanfoodname.tolist()  # transfer series to list
for i in range(len(nanfoodname)):
    df1=df[df['food'].str.match(nanfoodname[i]) & df['ounces'].notna()] # 按行筛选 build a df1 as inter df, which including non-nan values
    foodmean = df1['ounces'].mean()
    df.loc[df['food'].str.match(nanfoodname[i]) & df['ounces'].isnull(),'ounces'] = foodmean
    # set foodmean the nan which has the same food name， df.loc can select rows and columns, with rows has 2 condition and column'ounces'

df['ounces'] = df['ounces'].abs()
