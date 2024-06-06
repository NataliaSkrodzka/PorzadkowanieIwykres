import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xlsx = pd.ExcelFile('stacjepaliw.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)