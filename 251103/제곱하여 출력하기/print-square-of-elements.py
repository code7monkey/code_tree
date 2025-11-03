n = int(input())

lst = list(map(int,input().split()))

for i in range(n):
    print(lst[i]**2,end=' ')