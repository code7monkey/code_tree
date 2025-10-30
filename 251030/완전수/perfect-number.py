a,b = map(int, input().split())
cnt = 0

for i in range(a,b+1):
    lst = []
    for j in range(1,i):
        if i % j ==0:
            lst.append(j)
    if sum(lst) == i:
        cnt += 1

print(cnt)