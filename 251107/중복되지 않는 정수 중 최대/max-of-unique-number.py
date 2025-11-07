n = int(input())
lst = list(map(int, input().split()))

m = min(lst) - 1

for i in lst:
    if lst.count(i) >= 2:
        continue
    else:
        if i > m:
            m = i

if m < min(lst):
    print(-1)
else:
    print(m)