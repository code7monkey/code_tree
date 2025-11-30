A = input()

# Please write your code here.
def chk_palin(x):
    if x[::-1] == x:
        return 'Yes'
    return 'No'

print(chk_palin(A))