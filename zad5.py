import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xlsx=pd.ExcelFile('produkcja3.xlsx')
df=pd.read_excel(xlsx,header=0)
print(df)
df1=df.T
df1.reset_index(inplace=True)
print(df1)
df1.columns=['Rok','Wartość','Jednostka miary']
df1.drop([0],inplace=True)
print(df1)
ytickLab=[1.2, 1.3, 1.4, 1.5, 1.6]
ytickVal=[1200000, 1300000, 1400000, 1500000, 1600000]
plt.plot(df1['Rok'],df1['Wartość'])
plt.title('Wartość produkcji w poszczególnych latach')
plt.xlabel('Lata')
plt.ylabel('Wartość w mln zł')
plt.yticks(ytickVal, ytickLab)
plt.savefig('produkcji.pdf', format='pdf')
plt.show()