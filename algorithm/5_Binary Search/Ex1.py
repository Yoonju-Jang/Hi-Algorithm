# 떡볶이 떡 만들기

def binary_search(array, target, start, end):
    result = 0  # 최적화 height 찾기 위한 기록용
    while start <= end:
        total = 0  # 자르고 남은 떡 길이
        mid = (start + end)//2
        for x in array:
            if x > mid:
                total += x-mid
        if total < m:   # 왼쪽 탐색(height 더 작게)
            end = mid -1
        else:           # 오른쪽 탐색(height 더 크게)
            result = mid
            start = mid + 1 
    return result


# 떡의 개수(N), 요청한 떡의 길이(M) 입력
n, m = list(map(int,input().split()))
# 각 떡의 개별 높이 정보 입력
array = list(map(int,input().split()))


# 이진 탐색 수행 결과 출력
result = binary_search(array, m, 0, max(array))
print(result)