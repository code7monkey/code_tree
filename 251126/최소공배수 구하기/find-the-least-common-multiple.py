n, m = map(int, input().split())

def minn(x,y):
    i = 1
    while True:
        if i % x ==0 and i % y ==0:
            break
        else:
            i += 1 
    print(i)

minn(n,m)