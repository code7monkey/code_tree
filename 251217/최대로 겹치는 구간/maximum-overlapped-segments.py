n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 1.5 2.5 3.5 4.5 / 4.5 5.5 / 3.5 4.5
arr = [0] * 200 # -99.5=0, -98.5=1, .. -0.5=99, 0.5= 100 1.5 = 101 ... 99.5= 199 
for a, b in segments:
    for i in range(a+100, b+100):
        arr[i] += 1

print(max(arr))
