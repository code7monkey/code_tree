n = int(input())
lst = list(map(int,input().split()))

chk = []

for i in range(n-1,0,-1):
    for j in range(i-1,-1,-1):
        t = abs(lst[i]-lst[j])
        chk.append(t)

print(min(chk))