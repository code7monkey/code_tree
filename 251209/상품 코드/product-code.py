name, code = input().split()
code = int(code)

# Please write your code here.
class sangpoom:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code

ans1 = sangpoom()
print(f'product {ans1.code} is {ans1.name}')
ans2 = sangpoom(name,code) 
print(f'product {ans2.code} is {ans2.name}')  