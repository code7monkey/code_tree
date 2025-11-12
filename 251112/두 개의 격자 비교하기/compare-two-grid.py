n,m = map(int,input().split())
arr1 = []
arr2 = []

for _ in range(n):
    lst = list(map(int,input().split()))
    arr1.append(lst)

for _ in range(n):
    lst = list(map(int,input().split()))
    arr2.append(lst)

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()