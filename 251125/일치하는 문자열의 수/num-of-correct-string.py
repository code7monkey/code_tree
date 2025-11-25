a,b  = input().split()
a = int(a)

cnt = 0 

for _ in range(a):
    if input() == b:
        cnt += 1

print(cnt)