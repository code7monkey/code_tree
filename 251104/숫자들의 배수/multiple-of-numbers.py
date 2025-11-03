n = int(input())

i = 0
cnt = 0
while True:
    i += 1
    print(n*i,end=' ')
    if n*i % 5 ==0:
        cnt += 1
    
    if cnt ==2:
        break