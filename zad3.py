import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xlsx = pd.ExcelFile('lasy17.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

df1=pd.melt(df,id_vars=['Województwo'], var_name='Rok', value_name='Powierzchnia')
print(df1)
dfp=df1[df1['Województwo']=='POMORSKIE']
print(dfp)
dfo=df1[df1['Województwo']=='OPOLSKIE']
dfmp=df1[df1['Województwo']=='MAŁOPOLSKIE']
dfmz=df1[df1['Województwo']=='MAZOWIECKIE']

plt.figure(figsize=(8,6))
plt.scatter(dfp['Rok'],dfp['Powierzchnia'], s=12**2, label='Pomorskie', color='forestgreen', marker='o')
plt.scatter(dfo['Rok'],dfo['Powierzchnia'], s=12**2, label='Opolskie', color='sienna', marker='s')
plt.scatter(dfmp['Rok'],dfmp['Powierzchnia'], s=12**2, label='Małopolskie', color='deepskyblue', marker='*')
plt.scatter(dfmz['Rok'],dfmz['Powierzchnia'], s=12**2, label='Mazowieckie', color='aqua', marker='P')
plt.title('Powierzchnia lasów w poszczególnych województwach na przełomie lat', fontsize=13, fontweight='bold')
plt.xlabel('Lata', fontsize=12)
plt.ylabel('Powierzchnia', fontsize=12)
plt.legend(loc='best')
plt.savefig('powierzchniaLasow.png', format='png')
plt.show()