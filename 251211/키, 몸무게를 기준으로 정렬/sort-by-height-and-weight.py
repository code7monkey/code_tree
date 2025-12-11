n = int(input())

class kkkkk:
    def __init__(self, name, height, weight):
        self.nm = name
        self.hg = height
        self.wg = weight

lst = []
for _ in range(n):
    a,b,c = input().split()
    b = int(b); c = int(c)
    lst.append(kkkkk(a,b,c))

lst.sort(key = lambda x: (x.hg, -x.wg))

for i in lst:
    print(i.nm, i.hg, i.wg)