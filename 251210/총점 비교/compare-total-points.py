n = int(input())

class score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor  = kor
        self.eng  = eng
        self.math = math

lst = []
for _ in range(n):
    a,b,c,d = input().split()
    b = int(b); c = int(c); d = int(d)
    lst.append(score(a,b,c,d))

lst.sort(key=lambda x: x.kor + x.eng + x.math)

for i in lst:
    print(i.name, i.kor, i.eng, i.math)