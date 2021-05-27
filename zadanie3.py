#Zestaw B

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
import openpyxl

#zadanie3

dane = pd.read_csv('cars.csv',header=0,sep=';')
df = pd.DataFrame(dane)
pol = df[(df['Model year']>71)&(df['Model year']<78)].groupby(['Model year']).agg({'Car name':['count']})
wykres = pol.plot.bar()
plt.xticks(rotation=0)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Ilość wyprodukowanych aut w latach 72-77 ")
plt.show()