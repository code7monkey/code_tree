n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 1
        arr[j][i] = cnt

for lst in arr:
    for i in lst:
        print(i,end=' ')
    print()