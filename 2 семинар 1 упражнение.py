a = []
a = list(map(int, input().split()))
n = a[0]
index = -1;
for i in range(1, n + 1):
    ans = 0
    for j in range(n):
        if a[j] == i:
            ans = 1
            index = j
    if ans == 0 or index == 0:
        print(i)