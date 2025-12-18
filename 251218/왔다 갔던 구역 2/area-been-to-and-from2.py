n = int(input())
lst = []
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'L':
        a = -a
    lst.append(a)

# Please write your code here.
arr = [0] * 1001
start_idx = 500
for a in lst:
    if a > 0:
        for i in range(start_idx, start_idx + a):
            arr[i] += 1
        start_idx = start_idx + a
    else:
        for i in range(start_idx + a, start_idx):
            arr[i] += 1
        start_idx = start_idx + a

def over_two(lst):
    lst2 = []
    for i in lst:
        if i >= 2:
            lst2.append(i)
    return((len(lst2)))

print(over_two(arr))