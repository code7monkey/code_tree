lst = []
for _ in range(3):
    a,b = input().split()
    b = int(b)
    cond = -1
    if a =='Y' and b >= 37:
        cond = 0 
    elif a == 'N' and b >= 37:
        cond = 1
    elif a == 'Y' and b <37:
        cond = 2
    else:
        cond = 3
    lst.append(cond)

arr = [0] * 4
for i in lst:
    arr[i] += 1

for i in arr:
    print(i,end=' ')

if arr[0] >=2:
    print('E')