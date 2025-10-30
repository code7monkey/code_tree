n = int(input())
cnt =0

for i in range(n,0,-1):
    print('  '*(n-i),end='')
    for _ in range(1,i+1):
        cnt += 1
        if cnt == 10:
            cnt =1
        print(cnt,end=' ')    
    print()