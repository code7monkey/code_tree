n, m = map(int, input().split())

max_t = 1000
real_time = 0
ans = []
cnt = 0

pos_a, pos_b = [0] * (max_t + 1), [0] * (max_t +1)
state = [0] * (max_t + 1)

idx = 0
for _ in range(n):
    v, t = map(int, input().split())
    real_time += t
    for i in range(idx,idx +t):
        pos_a[i+1] = pos_a[i] + v
    idx = idx + t 

idx = 0 
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(idx,idx +t):
        pos_b[i+1] = pos_b[i] + v
    idx = idx + t 

for i in range(1, real_time + 1):
    state[i] = pos_a[i] - pos_b[i]

for i in range(1, real_time+1):
    if state[i] != 0:
        ans.append(state[i])

for i in range(len(ans)-1):
    if ans[i] * ans[i+1] < 0:
        cnt += 1

print(cnt)