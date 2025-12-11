class personal:
    def __init__(self, name, height, weight):
        self.nm = name
        self.hg = height
        self.wg = weight

lst = [ ]
for _ in range(5):
    a,b,c = input().split()
    b = int(b)
    lst.append(personal(a,b,c))

lst.sort(key=lambda x: x.nm)
print('name')
for i in lst:
    print(i.nm, i.hg, i.wg)

print()

lst.sort(key=lambda x: -x.hg)
print('height')
for i in lst:
    print(i.nm, i.hg, i.wg)
