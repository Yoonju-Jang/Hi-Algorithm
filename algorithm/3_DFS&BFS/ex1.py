# ex1) DFS-음료수 얼려 먹기
# 관건은 "연결요소찾기"

# 0: 방문x, 1: 방문0
# True: 아이스크림 생성, False: 아이스크림 생성x

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어날 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        global num
        num+=1
        print(x,y)
        # 해당 노드 방문 처리
        graph[x][y] = 1  
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        # 이는 아이스크림 갯수에 영향 x, 연결된 모든 노드에 대히여 방문 처리 수행(0->1) 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    # 현재 노드가 1 이라면 False
    return False


n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = [] 
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0   # 아이스크림 갯수 
l_num=[]
for i in range(n):
    for j in range(m):
        # 현위치에서 DFS 수행
        num=0
        if dfs(i, j) == True:
            result += 1
            l_num.append(num)

print(result)
for i in l_num:
    print(i)
# 아이스크림 시작점에서 dfs 수행
# -> 1) 주변 모든 노드를 연결(방문)
# -> 2) 시작점을 기준으로 아이스크림 1개만 생성