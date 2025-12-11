n = int(input())

class point:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.i = idx

lst = []
for i in range(1,n+1):
    x,y = map(int,input().split())
    lst.append(point(x,y,i))

lst.sort(key=lambda x: (abs(x.x)+abs(x.y)))

for ans in lst:
    print(ans.i)