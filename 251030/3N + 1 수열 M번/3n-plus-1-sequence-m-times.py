m = int(input())

for _ in range(m):
    n= int(input())
    cnt = 0
    while True:
        if n ==1:
            break
        elif n % 2 ==0:
            cnt += 1
            n //= 2
        else:
            cnt += 1
            n = 3*n +1
    print(cnt)