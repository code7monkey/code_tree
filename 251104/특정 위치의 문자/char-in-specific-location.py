lst = ['L','E','B','R','O','S']

m = input()

idx = -1

for i in range(6):
    if lst[i] == m:
        idx = i

if idx == -1:
    print('None')
else:
    print(idx)