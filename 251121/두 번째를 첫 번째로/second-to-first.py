s = input()
lst = list(s)
n = len(lst)

a = lst[0]
b = lst[1]

for i in range(n):
    if lst[i] == b:
        lst[i] = a

for i in range(n):
    print(lst,end='')