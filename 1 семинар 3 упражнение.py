import math
A = list(map(int, input().split()))
n= 0
c=1
for i in range(len(A)):
    n=n+1
    c=c*A[1];
b=c**(1/n)
print(b)
