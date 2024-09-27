numbers = list(map(int, input().strip().split()))
count = {}
for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
result = [i for i in numbers if count[i] == 1]
print(result)
