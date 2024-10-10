import csv
import matplotlib.pyplot as plt
with open('iris_data.csv', newline='') as f:
    r = csv.reader(f, delimiter=',')
    h = next(r)
    a = {}
    b = {'< 1.2 см': 0, '1.2 - 1.5 см': 0, '> 1.5 см': 0}
    for row in r:
        if len(row) < 6:
            continue
        s = row[5]
        p = float(row[3])
        if s in a:
            a[s] += 1
        else:
            a[s] = 1
        if p < 1.2:
            b['< 1.2 см'] += 1
        elif 1.2 <= p < 1.5:
            b['1.2 - 1.5 см'] += 1
        else:  # p >= 1.5
            b['> 1.5 см'] += 1
c = {key: value for key, value in b.items() if value > 0}
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(a.values(), labels=a.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Доля различных видов ирисов')
plt.subplot(1, 2, 2)
plt.pie(c.values(), labels=c.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Доли ирисов по длине лепестка')
plt.tight_layout()
plt.show()