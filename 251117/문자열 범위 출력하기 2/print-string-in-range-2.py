ss = input()
n = int(input())

m = len(ss)

if m > n:
    for i in range(-1,-n-1,-1):
        print(ss[i],end='')
else:
    for i in range(-1,-m-1,-1):
        print(ss[i],end='')