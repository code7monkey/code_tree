n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 0

if n % 2 ==0: 
    for j in range(n-1,-1,-1):
        if j % 2 ==1:
            for i in range(n-1,-1,-1):
                cnt += 1
                arr[i][j] = cnt
        else:
            for i in range(n):
                cnt += 1
                arr[i][j] = cnt
else:
    for j in range(n-1,-1,-1):
        if j % 2 ==0:
            for i in range(n-1,-1,-1):
                cnt += 1
                arr[i][j] = cnt
        else:
            for i in range(n):
                cnt += 1
                arr[i][j] = cnt 

for row in arr:
    print(*row)