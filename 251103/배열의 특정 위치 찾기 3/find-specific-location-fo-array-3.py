lst = list(map(int,input().split()))
n = len(lst)
s = 0

for i in range(n):
    if lst[i] == 0:
        t = i
        break

for i in range(t-1,t-4,-1):
    s += lst[i]
    
print(s)