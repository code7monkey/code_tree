n = int(input())

lst = list(map(int,input().split()))

class lining:
    def __init__(self, index, number):
        self.idx = index
        self.num = number

class answering:
    def __init__(self, adx, rdx):
        self.adx = adx
        self.rdx = rdx

ans = []
i = 0
for num in lst:
    i += 1
    ans.append(lining(i,num))

ans.sort(key=lambda x: x.num)

ans2= []

for rdx, p in enumerate(ans, start=1):
    ans2.append(answering(p.idx,rdx))

ans2.sort(key=lambda x: x.adx)

for i in ans2:
    print(i.rdx, end=' ')