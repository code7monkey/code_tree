n, m = map(int, input().split())

def maxx(a,b):
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            idx = i 
    print(idx)

maxx(n,m)