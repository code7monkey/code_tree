n = input()
m = input()
p = len(n)
t = len(m)
# Please write your code here.
def chk_idx():
    for i in range(p-t+1):
        if n[i:i+t] == m:
            return i
    return -1

print(chk_idx())
    