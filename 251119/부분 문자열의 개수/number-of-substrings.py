a = input()
b = input()

n = len(a)
m = len(b)

cnt = 0

for i in range(n-m+1):
    if a[i:i+m] == b:
        cnt += 1

print(cnt)