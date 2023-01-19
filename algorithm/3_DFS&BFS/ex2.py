# ex2) BFS-미로 탈출
# (1,1) -> (N,M), 괴물 존재(0)<->괴물 존재X(1)
# 미로 탈출을 위한 최소 칸의 개수(시작과 마지막 칸 모두 포함)

# BFS 소스코드 구현
def bfs

from collections import deque

n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = [] 
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))