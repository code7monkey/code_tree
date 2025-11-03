n = int(input())

lst = [1,n]

for i in range(10000):
    t = lst[i]+lst[i+1]
    lst.append(t)
    if t > 100:
        break

for i in lst:
    print(i,end=' ')