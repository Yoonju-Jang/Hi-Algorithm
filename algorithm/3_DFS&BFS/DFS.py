def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:   # 방문한적이 없다면
            dfs(graph, i, visited) # 재귀 사용

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],            # 인덱스 0을 Skip하고자
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
# '*9' : 인덱스 0을 Skip하고자
visited = [False]*9  

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


# 정리)
# visited : 노드의 방문기록 저장
# graph : 노드의 연결정보 저장