N, M = map(int, input().split())
MAX_T = 1000*1000

pos_a, pos_b = [0] * (MAX_T+1), [0] * (MAX_T+1)

time_a = 1
for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a-1] + v 
        time_a += 1

time_b = 1
for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b-1] + v 
        time_b += 1

state = 'N'
cnt = 0

for i in range(1,time_a):
    if pos_a[i] > pos_b[i]:
        if state != 'A':
            cnt +=1 
        state = 'A'
    elif pos_a[i] < pos_b[i]:
        if state != 'B':
            cnt +=1 
        state = 'B'
    else:
        if state != 'Both':
            cnt +=1
        state = 'Both'

print(cnt)