import csv
import matplotlib.pyplot as plt
from dateutil import parser
import numpy as np
a = []
b = []
with open('BTC_data.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        date = parser.parse(row[0])
        close = float(row[4])
        a.append(date)
        b.append(close)
dates_numeric = np.array([(date - a[0]).days for date in a])
coefficients = np.polyfit(dates_numeric, b, 3)
poly = np.poly1d(coefficients)
x_fit = np.linspace(dates_numeric.min(), dates_numeric.max(), 100)
y_fit = poly(x_fit)
plt.figure(figsize=(14, 7))
plt.plot(a, b, label='Цена закрытия биткоина', color='blue')
plt.plot([a[0] + np.timedelta64(int(x), 'D') for x in x_fit], y_fit, label='Полином 3-й степени', color='red')
plt.title('Историческая цена биткоина с полиномиальной аппроксимацией')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия (USD)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()