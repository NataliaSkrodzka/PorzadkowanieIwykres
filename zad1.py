import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xlsx = pd.ExcelFile('turystyka1.xlsx')
df=pd.read_excel(xlsx, header=0)
print(df.to_string())
df2=df.T
print(df2.to_string())
#df2.columns=['rok', 'ilosc']
#print(df2.to_string())
#df2['kategoria']=df2.index
#print(df2.to_string())
#df2.index=[x for x in range(30)]
df2.reset_index(inplace=True)
df2.columns=['kategoria', 'rok', 'ilosc']
print(df2.to_string())
df2['kategoria']=df2['kategoria'].str.replace('.1','')
df2['kategoria']=df2['kategoria'].str.replace('kategorii','')
df2['kategoria']=df2['kategoria'].str.replace('.2','')
df2['kategoria']=df2['kategoria'].str.replace('.3','')
df2['kategoria']=df2['kategoria'].str.replace('.4','')
df2['kategoria']=df2['kategoria'].str.replace('.5','')
print(df2.to_string())
df14=df2[df2['rok']==2014]
print(df14)
df15=df2[df2['rok']==2015]
df16=df2[df2['rok']==2016]
df17=df2[df2['rok']==2017]
df18=df2[df2['rok']==2018]
df19=df2[df2['rok']==2019]

plt.plot(df15['kategoria'],df15['ilosc'], ls='--', label='rok 2015')
plt.plot(df16['kategoria'],df16['ilosc'], ls=':', label='rok 2016')
plt.legend()
plt.xlabel('Kategoria hotelu')
plt.ylabel('Ilość hoteli')
plt.title('Ilość hoteli w poszczególnych kategoriach w latach 2015 i 2016')
plt.savefig('hotele.jpg', format='jpg')
plt.show()