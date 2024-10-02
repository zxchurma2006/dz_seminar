def gg_bb():
    x1 = input()
    y1 = input()
    x = [float(i) for i in x1.split(",")]
    y = [float(i) for i in y1.split(",")]
    return x, y
def izi_solo(x, y):
    N = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi**2 for xi in x)
    a = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / N
    return a, b
x, y = gg_bb()
a, b = izi_solo(x, y)
print(a)
print(b)