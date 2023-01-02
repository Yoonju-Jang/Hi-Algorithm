#10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)

# break문을 통해 반복문을 종료시킬 수 있다. 
# 단, continue는 다르다. skip의 기능

# 모범답안
# while(1):
#     a, b = map(int, sys.stdin.readline().split())
   
#     if a==b==0:
#         break
#     print(a+b)

# 배울점
# 1. while True 대신 while(1)
# 2. 여러줄 입력 받을땐 sys.stdin.readline()