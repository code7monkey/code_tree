n = int(input())

class weather:
    def __init__(self, date, day, weather):
        self.dt = date
        self.dy = day
        self.wt = weather

lst = []
for _ in range(n):
    a,b,c = input().split()
    lst.append(weather(a,b,c))

last_date = '2100-12-31'
for i in range(n):
    if lst[i].wt =='Rain':
        if lst[i].dt < last_date:
            last_date = lst[i].dt
            idx = i

ans = lst[idx]
print(ans.dt, ans.dy, ans.wt)