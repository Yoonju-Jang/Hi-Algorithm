# 1654번: 랜선 자르기

from sys import stdin

# 보유중 랜선 개수(K), 필요한 랜선 개수(N)
k, n = map(int,stdin.readline().split())
# 각 랜선의 개별 높이 정보 입력
array = [int(stdin.readline()) for _ in range(k)]

start = 1 
end = max(array)

result = 0    # 자를 랜선 길이
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 랜선 개수 계산
        if x >= mid:
            total += x // mid
    # 랜선 개수 부족한 경우 더 많이 자르기(왼쪽 탐색)
    if total < n:
        end = mid-1
    # 랜선 개수 충분할 경우 덜 자르기(오른쪽 탐색)
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록
        start = mid+1

print(result)