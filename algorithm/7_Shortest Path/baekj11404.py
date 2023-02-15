# 11404번: 플로이드
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수
# 2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력(단, 간선이 중복될수도)
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == INF:
        graph[a][b] = c
    else:  # 간선 중복시 > 최단 비용 택
        graph[a][b] = min(graph[a][b],c)

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
            print('0', end=" ")
        # 도달할 수 있는 경우 -> 거리
        else:
            print(graph[a][b], end=" ")
    print()