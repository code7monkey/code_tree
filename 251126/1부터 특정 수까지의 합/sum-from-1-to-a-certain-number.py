n = int(input())

def aaa(x):
    s = 0
    for i in range(1,x+1):
        s += i
    return s//10

print(aaa(n))