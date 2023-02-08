# 효율적인 화페 구성
# 입력
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# dp 테이블(구하고자 하는 m 까지만)
d = [10001] * (m + 1)

# 보텀업
d[0] = 0
for i in range(n):  # i - 화폐단위
    for j in range(array[i], m + 1):
        # (i-k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 출력
if d[m] == 10001:  # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])