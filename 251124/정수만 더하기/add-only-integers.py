lst = list(input())
s = 0

for i in lst:
    if i.isdigit() == True:
        s += int(i)

print(s)