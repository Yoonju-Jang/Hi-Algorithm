# 2776번: 암기왕
# 있으면 1 , 없으면 0
# 테스트 케이스(T)에 유의하자

# 수 찾기 함수 정의
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 입력
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()
    m = int(input())
    note_2 = list(map(int, input().split()))

    # note_2의 원소가 note_1에 담겼는지 확인
    for x in note_2:
        result = count_by_range(note_1,x,x)
        if result == 0:
            print(0)
        else:
            print(1)