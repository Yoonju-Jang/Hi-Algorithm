# 11053번: 가장 긴 증가하는 부분 수열

# 입력
n = int(input())
array = list(map(int, input().split()))

# dp 테이블
dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이
print(max(dp))