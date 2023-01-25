# ex2) BFS-미로 탈출
# (1,1) -> (N,M), 괴물 존재(0)<->괴물 존재X(1)
# 미로 탈출을 위한 최소 칸의 개수(시작과 마지막 칸 모두 포함)

# BFS 소스코드 구현
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4자기 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = [] 
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))