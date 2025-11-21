a = input()
b = input()

lst = list(a)
n = len(b)

b_list = list(b)

while True:
    found = False
    i = 0
    while i <= len(lst) - n:
        if lst[i:i+n] == b_list:
            lst = lst[:i] + lst[i+n:]
            found = True
            break
        i += 1

    if not found:  # 더 이상 제거할게 없으면 종료
        break

print(''.join(lst))
