n = int(input())
cnt = 64

for _ in range(n):
    for _ in range(n):
        cnt += 1
        print(chr(cnt),end='')
    print()