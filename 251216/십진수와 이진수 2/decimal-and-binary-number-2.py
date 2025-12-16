n = input()

# Please write your code here.
nums = 0 
for i in n:
    i = int(i)
    nums = nums * 2 + i

nums = 17 * nums

digits = []
while True:
    if nums < 2:
        digits.append(nums)
        break

    digits.append(nums%2)
    nums //= 2

for i in digits[::-1]:
    print(i,end='')