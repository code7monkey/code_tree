n = int(input())

x,y = 0,0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def conv_dir(t):
    if t == 'E':
        return 0
    elif t == 'S':
        return 1
    elif t == 'W':
        return 2
    else: 
        return 3

time = 0
is_time = False

for _ in range(n):
    dir, dist = input().split() 
    dist = int(dist)
    dir_num = conv_dir(dir)
    for _ in range(dist):
        x,y = x + dx[dir_num], y + dy[dir_num]
        time += 1
        if x == 0 and y ==0:
            print(time)
            is_time = True
    if is_time:
        break


if not is_time:
    print(-1)