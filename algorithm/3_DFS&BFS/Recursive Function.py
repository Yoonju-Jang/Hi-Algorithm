# 재귀함수: 자기 자신을 다시 호출하는 함수
# 사용할땐 종료 조건을 반드시 명시


## 1) STACK Frame 사용 입증
def rescursive_function(i):
    # 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    rescursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

rescursive_function(1)

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


## 3) 최대공약수 계산(유클리드 호제법)
# 두 자연수 A, B, and R(A를 B로 나눈 나머지)
# A와B의 최대공약수 == B와R의 최대공약수

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

print(gcd(192,162))