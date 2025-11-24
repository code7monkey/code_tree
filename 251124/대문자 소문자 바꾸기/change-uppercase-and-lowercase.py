s = input()
lst = list(s)
out = []

for i in lst:
    if i >= 'A' and i <= 'Z':
        out.append(i.lower())
    else:
        out.append(i.upper())

print(''.join(out))