n = 5 

class coded:
    def __init__(self, name, score):
        self.nm = name
        self.sc = score

lst = []
score_lst = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    score_lst.append(score)
    lst.append(coded(name,score))

for i in range(n):
    if lst[i].sc == min(score_lst):
        print(lst[i].nm, end=' ')
        print(lst[i].sc)
