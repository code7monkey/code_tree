n,m = map(int,input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for t in range(m):
    i,j = map(int,input().split())
    arr[i-1][j-1] = t+1

for row in arr:
    print(*row)