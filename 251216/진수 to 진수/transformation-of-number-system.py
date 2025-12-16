a, b = map(int, input().split())
n = input()

# Please write your code here.
nums = 0
for i in n:
    i = int(i)
    nums = a*nums + i

digits = []
while True:
    if nums < b:
        digits.append(nums)
        break

    digits.append(nums%b)
    nums //= b

for i in digits[::-1]:
    print(i,end='')