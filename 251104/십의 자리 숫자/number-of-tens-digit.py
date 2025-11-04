lst = list(map(int,input().split()))

arr = [0]*9
lst2 = []
for i in lst:
    if i == 0:
        break
    elif i < 10:
        continue
    else: 
        lst2.append(i//10)

for i in lst2:
    arr[i-1] += 1

i = 0
for j in arr: 
    i += 1
    print(f'{i} - {j}')