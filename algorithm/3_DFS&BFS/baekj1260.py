# 1260번: DFS와 BFS

#1) DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:   # 방문한적이 없다면
            dfs(graph, i, visited) # 재귀 사용


 #2) BFS 메서드 정의
from collections import deque

def bfs(graph, start, visited):
    print()
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 모두 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 입력 -> 인접 리스트 활용
from sys import stdin
n, m, v = map(int,stdin.readline().split())

graph = [[] for _ in range(n+1)] 

for _ in range(m):
    x, y  = map(int,stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    graph[i].sort()     # graph[3]=[4,1] 방지

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited_1 = [False]*(n+1)  
visited_2 = [False]*(n+1)  

# 정의된 DFS 함수 호출
dfs(graph, v, visited_1)
bfs(graph, v, visited_2)

