n = int(input())
cnt = 64

for i in range(1,n+1):
    for _ in range(1,i+1):
        cnt+=1
        if cnt == 91:
            cnt =65 
        print(chr(cnt),end='')
    print()