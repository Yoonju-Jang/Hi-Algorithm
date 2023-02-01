# 2512번: 예산
from sys import stdin

input = stdin.readline

n = int(input())   
array = list(map(int,input().split()))
m = int(input())   # 총 예산

start = 0
end = max(array)
result = 0    # 예산 상한액
if sum(array) <= m:
    print(end)
else: 
    while(start <= end):
        total = 0   # 상한액 적용을 받은 예산 총액
        mid = (start+end)//2
        for x in array:
            # 잘랐을 때의 예산 총액
            if x >= mid:
                total += mid
            else:
                total += x
        # 예산이 총액을 초과한 경우 더 많이 자르기(왼쪽 탐색)
        if total > m:
            end = mid-1
        # 예산이 총액에 여유있을 경우 덜 자르기(오른쪽 탐색)
        else:
            result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록
            start = mid+1
    print(result)
