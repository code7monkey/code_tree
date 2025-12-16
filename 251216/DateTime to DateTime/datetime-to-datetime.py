a, b, c = map(int, input().split())

# Please write your code here.
elapsed_time = 0
day, hour, mins = 11, 11, 11

while True:
    if b <= 11 and c < 11:
        elapsed_time = -1
        break

    if day == a and hour == b and mins ==c:
        break

    elapsed_time += 1
    mins += 1
    
    if mins == 60:
        hour +=1
        mins =0

    if hour == 24:
        day +=1
        hour = 0

print(elapsed_time)