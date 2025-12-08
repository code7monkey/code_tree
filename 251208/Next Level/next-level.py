u2_id, u2_lv = input().split()
u2_lv = int(u2_lv)

class next_level:
    def __init__(self, us_id='codetree', lv=10):
        self.idd = us_id
        self.lv = lv

us1 = next_level()
print(f'user {us1.idd} lv {us1.lv}')
us2 = next_level(u2_id, u2_lv)
print(f'user {us2.idd} lv {us2.lv}')
