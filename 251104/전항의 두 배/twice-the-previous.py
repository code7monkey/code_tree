lst = list(map(int,input().split()))

for i in range(8):
    lst.append(lst[i+1]+2*lst[i])

for i in lst:
    print(i,end=' ')