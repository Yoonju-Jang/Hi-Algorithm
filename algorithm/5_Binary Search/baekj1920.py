# 1920번: 수 찾기
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n = int(input())
a_array = list(map(int,input().split()))
a_array.sort()
m = int(input())
m_array = list(map(int,input().split()))

# m_array의 원소가 a_array에 담겼는지 확인
for x in m_array:
    result = count_by_range(a_array,x,x)
    if result == 0:
        print(0)
    else:
        print(1)