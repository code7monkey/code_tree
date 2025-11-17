n = int(input())
cnt = 0
ll = 0

for _ in range(n):
    ss = input()
    ll += len(ss)
    if ss[0] =='a':
        cnt += 1

print(ll,cnt)
