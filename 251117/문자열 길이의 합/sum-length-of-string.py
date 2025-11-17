n = int(input())
cnt = 0
ll = 0

for _ in range(n):
    ss = input()
    ll += len(ss)
    cnt += ss.count('a')

print(ll,cnt)
