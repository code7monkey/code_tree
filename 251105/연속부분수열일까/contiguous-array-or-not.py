na, nb = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

start = b[0]
lst = []

for i in range(na):
    if a[i] == start:
        lst.append(i)
cnt = 0
if len(lst) == 0:
    print('No')

for i in lst:
    a_chk = a[i:i+nb]
    for j,k in zip(a_chk,b):
        if j != k:
            print('No')
            break
        else:
            cnt += 1       
if cnt == nb:
    print('Yes')