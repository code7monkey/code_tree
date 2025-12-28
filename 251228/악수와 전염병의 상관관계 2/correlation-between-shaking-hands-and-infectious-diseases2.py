N, K, P, T = map(int, input().split())
events = [tuple(map(int, input().split())) for _ in range(T)]

infected = [0] * (N + 1)   # 1~N 사용
cnt = [0] * (N + 1)        # 감염된 후 악수 카운트

infected[P] = 1

events.sort(key=lambda x: x[0])  # 시간순

for t, x, y in events:
    # 현재 악수 시점에서 전염 가능한지(악수하기 "전" 상태로 판단)
    x_can = infected[x] and cnt[x] < K
    y_can = infected[y] and cnt[y] < K

    # 전염 처리 (전염 가능자 -> 상대가 미감염이면 감염)
    if x_can and not infected[y]:
        infected[y] = 1
    if y_can and not infected[x]:
        infected[x] = 1

    # 악수 카운트는 "감염자"면 증가 (감염자끼리도 포함)
    if infected[x]:
        cnt[x] += 1
    if infected[y]:
        cnt[y] += 1

print(''.join(map(str, infected[1:])))
