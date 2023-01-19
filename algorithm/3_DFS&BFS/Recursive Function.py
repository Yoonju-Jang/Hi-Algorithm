# 재귀함수: 자기 자신을 다시 호출하는 함수
# 재귀함수는 STACK Frame 사용
# 사용할땐 종료 조건을 반드시 명시
# DFS 구현할때 많이 사용

## 1)
# def rescursive_function(i):
#     # 종료 조건 명시
#     if i == 100:
#         return
#     print(i, '번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
#     rescursive_function(i+1)
#     print(i, '번째 재귀함수를 종료합니다.')

# rescursive_function(1)

## 2) 팩토리얼 구현

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_rescursive(n):
    if n <= 1: # n이 1이하인 경우 1을 반환
        return 1 
    # n! = n*(n-1)! 구현
    return n * factorial_rescursive(n-1)

print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_rescursive(5))