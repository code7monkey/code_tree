n = int(input())
cnt = 64

for i in range(n,0,-1):
    print('  '*(n-i),end='')
    for _ in range(i):
        cnt+= 1
        if cnt == 91:
            cnt = 65
        print(chr(cnt),end=' ')
    print()