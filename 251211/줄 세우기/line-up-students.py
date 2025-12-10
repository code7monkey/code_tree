n = int(input())

class lining:
    def __init__(self, height, weight, number):
        self.hg  = height
        self.wg  = weight
        self.num = number

lst=[]
for i in range(1,n+1):
    a,b = map(int,input().split())
    lst.append(lining(a,b,i))

lst.sort(key=lambda x: (-x.hg, -x.wg, x.num))

for i in lst:
    print(i.hg, i.wg, i.num)