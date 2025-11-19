a,b = input().split()

n = len(a)

for i in range(n):
    if a[i] == b:
        print(i)
        break

if i == n-1:
    print('No')