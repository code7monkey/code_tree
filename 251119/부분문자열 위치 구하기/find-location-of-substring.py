n = input()
m = input()

a = len(n)
b = len(m)

for i in range(a-b+1):
    if n[i:i+b] == m:
        print(i)
        break

if i == a-b:
    if n[i:i+b] != m:
        print(-1)
