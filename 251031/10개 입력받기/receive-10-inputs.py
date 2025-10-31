lst = list(map(int,input().split()))
s = 0
cnt = 0

for i in lst:
    if i ==0:
        break
    else:
        s += i
        cnt += 1

print(s,end=' ')
print(round(s/cnt,1))