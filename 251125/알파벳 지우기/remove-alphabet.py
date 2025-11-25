a = input()
b = input()

lst_a = list(a)
lst_b = list(b)
num_a = ''
num_b = ''

for i in lst_a:
    if i.isdigit() == True:
        num_a += i

for i in lst_b:
    if i.isdigit() == True:
        num_b += i

print(int(num_a)+int(num_b))