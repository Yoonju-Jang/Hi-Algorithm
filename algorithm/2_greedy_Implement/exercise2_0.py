# 구현 = 시뮬레이션 = 완전 탐색(가능한 경우의 수를 모두 검사)
# 2차원 공간 <=> 행렬(Matrix)
for i in range(5):
    for j in range(5):
        print('(',i,',',j,')',end=' ')
    print()

# 방향벡터(x-행, y-열)

#동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#현재 위치
x, y = 2, 2

for i in range(4):
    #다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx,ny)

# 예제)
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인하기
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)
        