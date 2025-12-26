n, m = map(int,input().split())

total_time = 0

a_lst = []
b_lst = []

a_spot = 0
b_spot = 0

printed = False

for _ in range(n):
    d, t = input().split()
    t = int(t)
    total_time += t
    if d == 'R':
        for i in range(t):
            a_lst.append(1)
    else:
        for i in range(t):
            a_lst.append(-1)

for _ in range(m):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(t):
            b_lst.append(1)
    else:
        for i in range(t):
            b_lst.append(-1)

for i in range(total_time):
    time =  i + 1
    a_spot += a_lst[i]
    b_spot += b_lst[i]
    if a_spot == b_spot:
        print(time)
        printed = True
        break

if not printed:
    print(-1)

    
