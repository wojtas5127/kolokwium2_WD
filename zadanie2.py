#Zestaw B

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
import openpyxl

#zadanie2

x1 = np.arange(-100, 100, 0.1)


y1 = -4*(x1**2)+(6*x1/2)+20
y2 = np.tan(x1)-5

plt.subplot(3, 1, 1)
plt.plot(x1, y1, 'ro',label='-4*(x1**2)+(6*x1/2)+20')
plt.title('Pierwszy wykres')
plt.grid(True)
plt.legend(loc='lower center')

plt.axis([-2, 4, -25, 25])


plt.subplot(3, 1, 2)
plt.plot(x1, y2, '-', label="tan(x)-5")
plt.title('Drugi wykres')
plt.ylabel('tan(x)-5')
plt.axis([-2, 6, -40, 80])
plt.legend(loc="lower left")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(x1, y1, 'ro',label='-4*(x1**2)+(6*x1/2)+20')
plt.title('Trzeci wykres')
plt.grid(True)
plt.plot(x1, y2, '-',label='np.tan(x2)-5')
plt.ylim(-100, 100)
plt.legend(loc='upper left')
plt.axis([-2, 6, -100, 100])

plt.show()