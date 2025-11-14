t = input()

lst = [
    'apple','banana','grape','blueberry','orange'
]

lst2 = []

cnt = 0

for i in range(5):
    s = lst[i]
    if s[2] == t or s[3] == t:
        cnt += 1
        lst2.append(s)

for i in lst2:
    print(i)

print(cnt)

        