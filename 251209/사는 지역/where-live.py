n = int(input())

class sanun:
    def __init__(self,name, code, area):
        self.name = name
        self.code = code
        self.area = area

lst = []
for _ in range(n):
    a,b,c = input().split()
    lst.append(sanun(a,b,c))

last_name = 'a'
for i in range(n):
    if lst[i].name > last_name:
        last_name = lst[i].name
        idx = i

print(f'name {lst[idx].name}')
print(f'addr {lst[idx].code}')
print(f'city {lst[idx].area}')