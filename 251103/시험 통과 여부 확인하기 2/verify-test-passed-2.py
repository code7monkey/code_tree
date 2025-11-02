n = int(input())
cnt = 0

for i in range(n):
    lst = list(map(int,input().split()))
    if sum(lst) >= 240:
        cnt += 1
        print('pass')
    else:
        print('fail')

print(cnt)