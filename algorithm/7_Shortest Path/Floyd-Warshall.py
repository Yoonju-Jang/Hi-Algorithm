INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수
start = int(input()) # 시작 노드 번호
# 2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c이다
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# 수행된 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우 -> 무한(INF)
        if graph[a][b] == INF:
            print('INFINITY', end=" ")
        # 도달할 수 있는 경우 -> 거리
        else:
            print(graph[a][b], end=" ")
    print()