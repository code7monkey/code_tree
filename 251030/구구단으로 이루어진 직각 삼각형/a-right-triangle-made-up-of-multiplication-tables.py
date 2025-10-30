n = int(input())

for i in range(n,0,-1):
    k = n+1-i
    for j in range(1,i+1):
        print(f'{k} * {j} = {k*j}',end=' ')
        if k + j < n+1:
            print('/',end=' ')
    print()