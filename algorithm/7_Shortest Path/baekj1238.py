# 1238번: 파티
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n, m, goal = map(int,input().split()) # 노드 개수, 간선 개수, 목적지
graph = [[] for _ in range(n+1)] # 인접 리스트

def dijkstra(start, goal):
    q = []
    distance = [INF]*(n+1)  # 함수 부를 때마다 > 최단 거리 테이블 초기화
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
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
    return distance[goal]


# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c이다
    graph[a].append((b,c))

# '오고 간다' -> 다익스트라 두 번 사용
solution = 0
for i in range(1,n+1):
    if i == goal: 
        continue
    solution = max( dijkstra(i,goal)+dijkstra(goal,i), solution)

print(solution)