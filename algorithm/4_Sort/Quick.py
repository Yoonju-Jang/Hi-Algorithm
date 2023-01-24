# 퀵 정렬: 분할(피벗을 기준으로 데이터 묶음) -> 왼/오 데이터 정렬
# 왼쪽(피벗보다 큰 데이터) - 오른쪽(피벗보다 작은 데이터)
# 시간 복잡도는 평균적으로 O(NlogN)
# !but! 이미 정렬된 배열에 대해선 O(N^2)

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫번째 원소
    left = start + 1
    right = end
    while(left<=right): # 엇갈리기 전까지 진행
        # 왼쪽에서 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1  # left(피벗보다 큰 데이터 인덱스)
        # 오른쪽에서 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1  # right(피벗보다 작은 데이터 인덱스)
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽/오른쪽 부분 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)



quick_sort(array, 0, len(array)-1)
print(array)