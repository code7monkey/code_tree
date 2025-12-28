N, K, P, T = map(int, input().split())
events = [tuple(map(int, input().split())) for _ in range(T)]
events.sort(key=lambda x: x[0])

infected = [0] * (N + 1)  # 1~N
cnt = [0] * (N + 1)       # 감염된 "이후" 악수 횟수

infected[P] = 1

for t, x, y in events:
    pre_x = infected[x]
    pre_y = infected[y]

    x_can = pre_x and cnt[x] < K
    y_can = pre_y and cnt[y] < K

    # 전염 (악수 직전 상태 기준으로만)
    if x_can and not infected[y]:
        infected[y] = 1
    if y_can and not infected[x]:
        infected[x] = 1

    # 악수 카운트는 "악수 직전 감염자"만 증가
    if pre_x:
        cnt[x] += 1
    if pre_y:
        cnt[y] += 1

print(''.join(map(str, infected[1:])))

