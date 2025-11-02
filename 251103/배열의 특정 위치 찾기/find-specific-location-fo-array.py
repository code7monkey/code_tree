lst = list(map(int,input().split()))

n = len(lst)
s = 0

for i in range(0,n,2):
    s += lst[i]
print(s,end=' ')

cnt = 0
s  = 0

for i in range(3,n,3):
    s += lst[i]
    cnt += 1

m = s/cnt
print(round(m,1))