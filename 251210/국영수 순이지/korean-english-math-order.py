n = int(input())

class score:
    def __init__(self, name, korean, english, math):
        self.nam = name
        self.kor = korean
        self.eng = english
        self.mat = math

lst = []
for _ in range(n):
    a,b,c,d = input().split()
    b = int(b)
    c = int(c)
    d = int(d)
    lst.append(score(a,b,c,d))

lst.sort(key=lambda x:(-x.kor, -x.eng, -x.mat))

for ans in lst:
    print(ans.nam, ans.kor, ans.eng, ans.mat)