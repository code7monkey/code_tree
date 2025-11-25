a = input()
b = input()

n = len(a)
cnt = 0

for _ in range(n): 
    a = a[-1] + a[:-1]
    cnt += 1
    if a == b:
        break

if cnt == n:
    print(-1)
else: 
    print(cnt)