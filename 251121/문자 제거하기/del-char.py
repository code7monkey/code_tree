s = input()
lst = list(s)
n = len(lst)

while len(lst) >= 2:
    i = int(input())
    if i < n:
        lst.pop(i)
    else:
        lst.pop(-1)
    s = ''.join(lst)
    print(s)