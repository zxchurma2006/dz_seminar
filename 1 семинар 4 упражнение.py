f = open('../../input.txt')
k=0
B=[]
A=[]
lines=f.readlines()
for i in range(len(lines)):
    if i==len(lines)-1:
        B.append(lines[i])
    else:
        A=list(map(int,lines[i].split()))
if B[0]=="+" :
    c=0
    for i in range(len(A)):
        c=c+A[i];
elif B[0]=="-" :
    c=0
    for i in range(len(A)):
        c=c-A[i];
else:
    c=1
    for i in range(len(A)):
        c=c*A[i];
q = open('../../output.txt', 'w')
q.write(str(c))
f.close()
q.close()


