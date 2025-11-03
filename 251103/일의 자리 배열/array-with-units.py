lst = list(map(int,input().split()))

for _ in range(8):
    lst.append(0)

for i in range(2,10):
    lst[i] = (lst[i-1] + lst[i-2]) % 10

for i in range(10):
    print(lst[i],end=' ')