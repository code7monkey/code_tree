s = input()
lst = list(s)
out = []

for i in lst:
    if i.isalpha() == True:
        out.append(i.lower())
    elif i.isdigit() == True:
        out.append(i)

s = ''.join(out)
print(s)