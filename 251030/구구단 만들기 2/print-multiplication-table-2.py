a,b = map(int,input().split())

lst =[2,4,6,8]

for i in lst:
    for j in range(b,a-1,-1):
        print(f'{j} * {i} = {j*i}',end=' ')
        if j > a:
            print('/',end=' ')
    print()