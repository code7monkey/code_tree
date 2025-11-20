ss = input()

n = len(ss)
a = ss[0]
b = ss[1]

lst = list(ss)

for i in range(n):
    if lst[i] == a:
        lst[i] = b
    elif lst[i] == b:
        lst[i] = a

for i in range(n):
    print(lst[i],end='')