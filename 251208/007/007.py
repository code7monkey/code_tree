secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class zerozero7:
    def __init__(self, sc, mp, t):
        self.sc = sc
        self.mp = mp 
        self.t  = t

zeor_7 = zerozero7(secret_code, meeting_point, time)
print(f'secret code : {zeor_7.sc}')
print(f'meeting point : {zeor_7.mp}')
print(f'time : {zeor_7.t}')