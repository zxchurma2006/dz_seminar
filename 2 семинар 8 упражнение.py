import random
N = int(input())
elements = list(map(int, input().split()))
median_i = N // 2
left = 0
right = N - 1
while True:
    if left == right:
        median = elements[left]
        break
    a = random.randint(left, right)
    b = elements[a]
    elements[a], elements[right] = elements[right], elements[a]
    c = left
    for i in range(left, right):
        if elements[i] < b:
            elements[c], elements[i] = elements[i], elements[c]
            c += 1
    elements[c], elements[right] = elements[right], elements[c]
    if median_i == c:
        median = elements[c]
        break
    elif median_i < c:
        right = c - 1
    else:
        left = c + 1
print(median)