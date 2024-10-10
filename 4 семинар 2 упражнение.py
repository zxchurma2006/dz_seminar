import matplotlib.pyplot as plt
import numpy as np
n = [0, 0, 1, 2, 4, 7, 18, 16, 22, 26, 33, 23, 18, 10, 6, 4, 7, 0]
omega = [0, 0, 0.005, 0.01, 0.02, 0.035, 0.09, 0.08, 0.11, 0.13, 0.165, 0.115, 0.09, 0.05, 0.03, 0.02, 0.035, 0]
x2 = [1, 1, 0, 0, 2, 2, 7, 8, 7, 11, 16, 18, 17, 11, 20, 15, 10, 11,10 ,10 1, 5, 1]
y2 = (0.005, 0.005, 0, 0, 0.01, 0.01, 0.035, 0.04, 0.035, 0.055, 0.08, 0.14, 0.085, 0.055, 0.01, 0.075, 0.05, 0.055, 0.05, 0.05, 0.025, 0.005)
plt.figure(figsize=(12, 6))
bar_width = 0.4
bar_positions = np.arange(len(n))
plt.bar(bar_positions, omega, width=bar_width, color='blue', alpha=0.5, label='ω от n1')
bar_positions_2 = np.array(x2) + bar_width
plt.bar(bar_positions_2, y2, width=bar_width, color='orange', alpha=0.5, label='ω от n2')
plt.xlabel('n')
plt.ylabel('ω')
plt.title('Гистограммы зависимости ω от n и второй набор данных')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()