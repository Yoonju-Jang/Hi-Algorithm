# 1) 1이 될 때까지 :80점
# N에서 1을 빼기 OR N을 K로 나누기
 
N, K = map(int, input().split())

cnt = 0
while(1):
    if N==1:
        break
    if N % K == 0: N /= K
    else: N-=1
    cnt+=1
print(cnt)

# 시간복잡도를 줄이는 code(hard)
n, k = map(int, input().split())

result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k  # 가장 근처의 배수값 찾기
    result += (n-target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을때) 반복문 탈출:
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
