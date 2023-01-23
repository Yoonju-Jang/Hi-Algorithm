# 2667번
# 1(집 보유->타깃) <-> 0(집 없음->관심x)
# True: 단지 생성, False: 단지 생성x

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):

    # 주어진 범위를 벗어날 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        global house
        house += 1
        # 해당 노드 방문 처리
        graph[x][y] = 0 
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        # 이는 단지 수에 영향 x, 연결된 모든 노드에 대히여 방문 처리 수행(1->0) 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    # 현재 노드가 0 이라면 False   
    return False

## 입력
from sys import stdin
n = int(input())

# 2차원 리스트의 맵 정보 입력 받기
graph = [] 
for _ in range(n):
    graph.append(list(map(int,stdin.readline().rstrip())))
    # rstrip() 꼭 사용해야 함!

# 모든 노드(위치)에 대하여 집 탐색
housing = 0  # 단지 수
h_num=[]     # 단지에 속한 집 갯수
for i in range(n):
    for j in range(n):
        house=0   # 단지 초기화
        if dfs(i, j) == True:
            housing += 1
            h_num.append(house)

print(housing)
h_num.sort()
for h in h_num:
    print(h)