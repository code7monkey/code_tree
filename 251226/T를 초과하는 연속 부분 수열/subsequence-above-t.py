n, t = map(int,input().split())

lst = list(map(int,input().split()))

max_len = 0
cur_len = 0 

for i in range(n):
    if lst[i] > t:
        cur_len += 1
    else:
        max_len = max(max_len,cur_len)
        cur_len = 0

max_len = max(max_len, cur_len)
print(max_len)