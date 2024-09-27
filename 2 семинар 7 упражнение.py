numbers = list(map(int, input().split()))
maxl = 0
maxi = 0
for i in numbers:
    count = numbers.count(i)
    if count > maxl:
        maxl = count
        maxi = i
print(maxi)