A = input()

# Please write your code here.
def chk_a(x):
    if len(set(x)) ==1:
        print('No')
    else:
        print('Yes')

chk_a(A)