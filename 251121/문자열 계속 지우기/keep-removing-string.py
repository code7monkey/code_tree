a = input()
b = input()
n = len(b)

while a.find(b) != -1:
    idx = a.find(b)
    a = a[:idx] + a[idx+n:]

print(a)