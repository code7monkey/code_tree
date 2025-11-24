s = input()
m = input()
lst = list(m)

for i in lst:
    if i == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]

print(s)