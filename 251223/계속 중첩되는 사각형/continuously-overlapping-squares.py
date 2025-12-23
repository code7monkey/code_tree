size = 201
offset = 100

arr = [[0]*size for _ in range(size)]

n = int(input())

# 빨-파-빨-파
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    # 빨간색
    if i % 2 ==0:
        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x][y] = 0
    # 파란색
    else:
        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x][y] = 1

ans = 0 
for x in range(size):
    for y in range(size):
        ans += arr[x][y]

print(ans)

