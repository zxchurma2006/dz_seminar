import matplotlib.pyplot as plt
import numpy as np
n = [0, 0, 1, 2, 4, 7, 18, 16, 22, 26, 33, 23, 18, 10, 6, 4, 7, 0]
omega = [0, 0, 0.005, 0.01, 0.02, 0.035, 0.09, 0.08, 0.11, 0.13, 0.165, 0.115, 0.09, 0.05, 0.03, 0.02, 0.035, 0]
plt.figure(figsize=(12, 6))
plt.bar(range(len(n)), omega, tick_label=n)
plt.xlabel('n')
plt.ylabel('ω')
plt.title('Гистограмма зависимости ω от n')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()