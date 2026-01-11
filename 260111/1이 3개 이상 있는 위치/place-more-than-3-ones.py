n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_ran(x,y):
    return 0 <= x and x < n and 0 <= y and y <n

cnt = 0

for x in range(n):
    for y in range(n):
        pro_cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_ran(nx,ny) and arr[nx][ny] == 1:
                pro_cnt += 1
        if pro_cnt >=3:
            cnt += 1
print(cnt)

