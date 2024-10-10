import csv
import matplotlib.pyplot as plt
from dateutil import parser
a = []
b = []
with open('BTC_data.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        date = parser.parse(row[0])
        close = float(row[4])
        a.append(date)
        b.append(close)
plt.figure(figsize=(14, 7))
plt.plot(a, b, label='Цена закрытия биткоина', color='blue')
plt.title('Историческая цена биткоина')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия (USD)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))
plt.show()