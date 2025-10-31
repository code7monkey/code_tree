lst = list(map(int,input().split()))

n = len(lst)
for i in range(n-1,-1,-1):
    if lst[i] ==0:
        continue
    else:
        print(lst[i],end=' ')