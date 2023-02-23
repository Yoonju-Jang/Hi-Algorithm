# 1647번: 도시 분할 계획
# Find (경로 압축)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집 개수와 도로 개수 입력 받기
n, m = map(int, input().split())
parent = [0] * (n+1)   # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i 

# 모든 간선에 대한 정보 입력 받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 적은 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
real_c = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        real_c = cost
        result += real_c

print(result - real_c)