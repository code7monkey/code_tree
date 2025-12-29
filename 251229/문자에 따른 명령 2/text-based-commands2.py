x,y = 0,0
dx, dy = [1, 0 , -1, 0], [0, -1, 0, 1]
dir_num = 3

lst = list(input())

def convert_dir(t):
    global x,y,dir_num
    if t == 'R':
        dir_num = (dir_num+1) % 4
    elif t == 'L':
        dir_num = (dir_num-1+4) %4
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]

for i in lst:
    convert_dir(i)

print(x, y)
