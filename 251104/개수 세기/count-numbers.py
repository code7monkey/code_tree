n, m =map(int,input().split())
lst = list(map(int,input().split()))
idx = -1

for i in range(n):
    if lst[i] == m:
        print(i+1)