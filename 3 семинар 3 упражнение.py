def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        nod, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return nod, x, y
print(extended_euclidean(int(input()),int(input())))