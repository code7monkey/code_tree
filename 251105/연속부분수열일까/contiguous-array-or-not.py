na, nb = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

start = b[0]
lst = []

for i in range(na):
    if a[i] == start:
        lst.append(i)

if len(lst) == 0:
    print('No')

chk = 0

for i in lst:
    cnt = 0
    a_chk = a[i:i+nb]
    for j,k in zip(a_chk,b):
        if j != k:
            break
        else:
            cnt += 1       
    if cnt == nb:
        print('Yes')
        chk = 1

if chk == 0:
    print('No')