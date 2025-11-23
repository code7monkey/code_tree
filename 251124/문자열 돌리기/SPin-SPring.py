s = input()

n = len(s)

print(s)
for _ in range(n):
    s = s[-1] + s[:-1]
    print(s)