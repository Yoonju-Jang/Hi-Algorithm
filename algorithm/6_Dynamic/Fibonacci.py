# 1) 재귀 -> 중복되는 부분 문제 발생
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 2) 다이나믹1(탑다운)

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# 3) 다이나믹2(보텀업)

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

# 반복문 구현
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])