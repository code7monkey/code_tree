a, b = input().split()

lst_a = list(a)
lst_b = list(b)

s=0

for lst in (lst_a,lst_b):
    z = ''
    for i in lst:
        if i.isdigit() ==False:
            break
        else:
            z += i
    z = int(z)
    s += z

print(int(s))