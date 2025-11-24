s = input()
lst = list(s)
o = []
for i in lst:
    if i.isalpha() == True:
        o.append(i)

s = ''.join(o).upper()
print(s)