# 계수 정렬: 각각의 데이터가 몇번씩 등장했는가
# 특정 조건에 부합할 때만 사용가능/ 매우 빠른 성능
# 동일한 값을 가지는 데이터가 여러개 등장할때 매우 효과적
# 시간-공간 복잡도는 O(N+K)

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)  # 0 ~ 최댓값

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): 
    for j in range(count[i]): 
        print(i, end=' ') # 데이터 등장 횟수만큼 인덱스 출력