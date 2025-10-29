a,b = map(int,input().split())

lst = []
for i in range(b,a-1,-1):
    if i % 2 ==0:
        lst.append(i)

k = min(lst)

for i in range(1,10):
    for j in lst:
        print(f'{j} * {i} = {j*i}',end=' ')
        if j > k:
            print('/',end=' ')
    print()