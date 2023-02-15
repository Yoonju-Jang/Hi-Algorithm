INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드 개수, 간선 개수
n, m= map(int,input().split()) 
# 2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    # 비용은 1로 고정, 양방향 간선
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 k와 최종 목적지 노드 x
x, k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 
if distance >= INF:
    print('-1')
# 도달할 수 있다면 > 최단 거리 출력
else:
    print(distance)