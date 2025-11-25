cnt = 0
lst = []

while True:
    s = input()
    if s == '0':
        break
    else:
        if cnt % 2 ==0:
            lst.append(s)
        cnt += 1

print(cnt)
for i in lst:
    print(i)