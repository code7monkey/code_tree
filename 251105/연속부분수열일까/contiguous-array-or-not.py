na, nb = map(int,input().split())

if na < nb:
    print('No')

break

a = list(map(int,input().split()))
b = list(map(int,input().split()))

start = b[0]

idx = -1
for i in range(na):
    if a[i] == start:
        idx = i
        break

a_chk = a[idx:idx+nb]

cnt = 0

for i,j in zip(a_chk,b):
    if i != j:
        print('No')
        break
    else:
        cnt +=1

if cnt == nb:
    print('Yes')