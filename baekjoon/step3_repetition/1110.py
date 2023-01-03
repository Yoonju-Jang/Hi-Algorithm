#1110
N = int(input())

while True:
    if N>=10:
    else:
        new = N*10 + N

# 내 실수 - 무조건 if/else로 조건 세분화시킴

#모범답안
#자릿수가 중요할때? -> //(몫),%(나머지)를 유용하게 활용하라

N = int(input())
num = N
cnt = 0      # 사이클 수 

while True:
    a = num // 10
    b = num % 10 
    c = (a+b)%10      # 중요도: 자릿수를 더한 값 < 자릿수를 더한 값의 가장 오른쪽 수
    num = (b*10) + c  # 새로운 수 생성
    
    cnt = cnt+1
    if(num==N):
        break

print(cnt)
