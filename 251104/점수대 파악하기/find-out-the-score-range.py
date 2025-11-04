lst = list(map(int,input().split()))

arr = [0] * 10
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

i = 100
for j in range(9,-1,-1):
    p = arr[j]
    print(f'{i} - {p}')
    i -= 10