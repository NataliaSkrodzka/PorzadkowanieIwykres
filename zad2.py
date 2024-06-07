import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xlsx = pd.ExcelFile('stacjepaliw.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

df1 = pd.melt(df,id_vars=['Nazwa'], var_name='Rok',value_name='Ilość')
print(df1)
dfs=df1[df1['Nazwa']=='ŚLĄSKIE']
print(dfs)
dfm=df1[df1['Nazwa']=='MAŁOPOLSKIE']
print(dfm)

plt.plot(dfs['Rok'],dfs['Ilość'], label='Śląskie')
plt.plot(dfm['Rok'],dfm['Ilość'], label='Małopolskie')
plt.xlabel('Lata')
plt.ylabel('Ilość stacji')
plt.title('Ilość stacji paliw w 2 województwach na przedziale lat')
plt.legend()

plt.savefig('stacjepaliw.png', format='png')
plt.show()