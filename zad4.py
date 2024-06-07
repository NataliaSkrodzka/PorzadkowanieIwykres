import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('rod12.csv', sep=';', header=0)
print(df)
df1 = df.T
print(df1)
#df2=pd.pivot(df,columns='Rodzaje terenu', values=['ogrody', 'ogrody.1')
df1.reset_index(inplace=True)
print(df1)
df1.columns=['Rodzaje terenu', 'Ogrody', 'Rok', 'Wartość', 'Jednostka miary']
print(df1)
df1.drop(index=0, inplace=True)
print(df1)
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.1','')
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.2','')
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.3','')
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.4','')
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.5','')
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.6','')
df1['Rodzaje terenu']=df1['Rodzaje terenu'].str.replace('.7','')
print(df1)
df2 = df1.pivot(columns='Ogrody', values=['Wartość'])
print(df2)