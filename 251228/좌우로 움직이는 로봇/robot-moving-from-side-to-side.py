n, m = map(int, input().split())

max_t = 1000000

pos_a, pos_b = [0] * (max_t + 1), [0] * (max_t + 1)

time_a = 1

for _ in range(n):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1

for _ in range(m):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

if time_a > time_b:
    for i in range(time_b, time_a):
        pos_b[i] = pos_b[i-1]
else:
    for i in range(time_a, time_b):
        pos_a[i] = pos_a[i-1]

cnt = 0
time = max(time_a,time_b)

for i in range(1,time):
    if pos_a[i] == pos_b[i]:
        if pos_a[i-1] != pos_b[i-1]:
            cnt += 1

print(cnt)  
