s = 0

for i in range(1,5):
    lst = list(map(int,input().split()))
    for j in range(i):
        s += lst[j]

print(s)