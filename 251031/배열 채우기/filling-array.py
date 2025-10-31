p_lst = list(map(int,input().split()))
lst= []
for i in p_lst:
    lst.append(i)
    if i == 0:
        break

n = len(lst)
for i in range(n-1,-1,-1):
    if lst[i] ==0:
        continue
    else:
        print(lst[i],end=' ')