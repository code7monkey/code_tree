code, color, sec = input().split()
sec = int(sec)

class bomb:
    def __init__(self, code, color, sec):
        self.cd = code
        self.cl = color
        self.sc = sec

ans = bomb(code,color,sec)
print(f'code : {ans.cd}')
print(f'color : {ans.cl}')
print(f'second : {ans.sc}')