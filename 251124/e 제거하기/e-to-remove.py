s = input()
n = len(s)
lst = list(s)

for i in range(n):
    if lst[i] == 'e':
        idx = i
        break

lst.pop(idx)
s = ''.join(lst)
print(s)