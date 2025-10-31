s = 0
cnt = 0
lst = list(map(int,input().split()))

for i in range(10):
    x = lst[i]
    if x <250:
        s += x
        cnt += 1
    else:
        break

print(s,end=' ')
print(round(s/cnt,1))