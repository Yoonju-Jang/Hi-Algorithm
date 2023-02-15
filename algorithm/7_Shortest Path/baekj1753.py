# 1753번: 최단경로
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

v, e = map(int,input().split()) # 노드 개수, 간선 개수
k = int(input()) # 시작 노드 번호
graph = [[] for _ in range(v+1)] # 인접 리스트
distance = [INF]*(v+1)  # 최단 거리 테이블 > 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(e):
    u, v, w = map(int, input().split())
    # u번 정점에서 v번 정점으로 가는 비용이 w이다
    graph[u].append((v,w))


def dijkstra(k):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, k))
    distance[k] = 0
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
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for dis in distance[1:]:
    print(dis if dis != INF else 'INF')
