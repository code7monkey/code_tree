n, m = map(int, input().split())

# Please write your code here.
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
cnt = -1

for i in range(m):
    if i % 2 ==0:
        for j in range(n):
            cnt += 1
            arr[j][i] = cnt
    else:
        for j in range(n-1,-1,-1):
            cnt += 1
            arr[j][i] = cnt

for lst in arr:
    for i in lst:
        print(i,end=' ')
    print()