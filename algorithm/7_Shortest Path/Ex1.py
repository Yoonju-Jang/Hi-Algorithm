import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드 개수, 간선 개수, 시작 노드
n, m, start = map(int,input().split()) 
graph = [[] for i in range(n+1)] # 인접 리스트
distance = [INF]*(n+1)  # 최단 거리 테이블 > 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z이다
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

# 결과 출력
cnt = 0     # 도달할 수 있는 노드 개수
max_dist = 0  # 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    if d != INF:
        cnt += 1 
        max_dist = max(max_dist, d)

# 시작 노드는 제외해야 하므로 cnt-1
print(cnt-1, max_dist)