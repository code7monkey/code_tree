p_lst = list(map(int,input().split()))
tw_cnt=0
s = 0

for i in p_lst:
    if i ==0:
        break
    elif i % 2 ==0:
        tw_cnt += 1
        s += i

print(tw_cnt,s,sep=' ')