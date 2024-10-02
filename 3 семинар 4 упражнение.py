line = input()
size, symb = line.split()
size = int(size)
for i in range(1, (size // 2) + 2):
    print(symb * i)
for i in range((size // 2), 0, -1):
    print(symb * i)
