n, m = map(int, input().split())
lst = list(map(int, input().split()))
arr = []
# Please write your code here.
def sum_m():
    arr.append(lst[m-1])

while m != 1:
    sum_m()
    if m % 2 == 1:
        m -= 1
    else:
        m //= 2

print(sum(arr)+lst[0])