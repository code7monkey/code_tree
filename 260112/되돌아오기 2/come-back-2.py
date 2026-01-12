lst = list(input())

x,y = 0,0
dir_num = 3 

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

time = 0
is_end = False

for i in lst:
    if is_end:
        break
    if i == 'F':
        x,y = x + dx[dir_num], y + dy[dir_num]
        time += 1
        if x == 0 and y ==0:
            is_end = True
            print(time) 
    elif i == 'R':
        dir_num = (dir_num+1)%4
        time += 1
    else:
        dir_num = (dir_num+3)%4
        time += 1

if not is_end:
    print(-1)

