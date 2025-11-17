aa = input()

n = len(aa)

cnt = 1
lst = []

for i in range(n-1):
    if i == n-2:
        if aa[i] == aa[i+1]:
            cnt += 1
            lst.append(aa[i])
            lst.append(cnt)
        else:
            lst.append(aa[i])
            lst.append(cnt)
            lst.append(aa[i+1])
            lst.append(1)
    elif aa[i] == aa[i+1]:
       cnt += 1
    else:
        lst.append(aa[i])
        lst.append(cnt)
        cnt = 1 

ll = 0

for i in lst:
    ll += len(str(i))

print(ll)

for i in lst:
    print(i,end='')
