s = input()
lst = list(s)

while len(lst) >= 2:
    i = int(input())
    if i < len(lst):
        lst.pop(i)
    else:
        lst.pop(-1)
    s = ''.join(lst)
    print(s)