number = int(input())
if number <= 1:
    print("число должно быть больше 1((")
mn = []
while number % 2 == 0:
    mn.append(2)
    number //= 2
for i in range(3, int(number ** 0.5) + 1, 2):
    while number % i == 0:
        mn.append(i)
        number //= i
if number > 2:
    mn.append(number)
print(mn)
