# L: 반시계, R: 시계

dx = [1, 0 , -1, 0]
dy = [0, -1, 0, 1]

x,y = 0,0
dir_num = 3

def diiir(i):
    global x, y, dir_num
    if i == 'L':
        dir_num = (dir_num + 3) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

lst = list(input())

for i in lst:
    diiir(i)

print(x, y)
    