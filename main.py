#Zestaw B

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
import openpyxl

#zadanie1

dane = pd.read_csv('cars.csv',header=0,sep=';')
df = pd.DataFrame(dane)

pol1 = pd.DataFrame(df[df['Horsepower'] > 105])
# print(pol1)

pol2 = pd.DataFrame(df.groupby(['Model year'])['Car name'].count())
# print(pol2)

wykres = pol2.plot.pie(subplots=True,autopct='%.2f %%',fontsize=10,figsize=(6,6),legend=False)
plt.title("Suma pojazdów wyprodukowana w danym roku")
plt.savefig('wykres.png')
plt.show()

