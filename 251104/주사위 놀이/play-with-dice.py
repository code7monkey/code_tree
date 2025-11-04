lst = list(map(int,input().split()))
arr = [0]*6

for i in lst:
    arr[i-1] += 1

i = 0
for j in arr:
    i += 1
    print(f'{i} - {j}')