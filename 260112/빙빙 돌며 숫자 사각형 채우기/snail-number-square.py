n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0

# 시작은 1로
arr[x][y] = 1

# for문 2 ~ m*n까지의 숫자를 넣는거
for i in range(2,m*n+1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if in_range(nx, ny) and arr[nx][ny] == 0:
        x, y = nx, ny
        arr[x][y] = i

    else:
        dir_num = (dir_num+1) % 4
        x, y = x + dx[dir_num], y + dy[dir_num]
        arr[x][y] = i

for lst in arr:
    for i in lst:
        print(i, end=' ')
    print()