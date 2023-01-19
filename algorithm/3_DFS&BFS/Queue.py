# 큐 : 입구와 출구가 모두 뚫려 있는 터널 형태
# 리스트로 구현 가능하지만 시간 비효율 
# -> deque 라이브러리 사용

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue)  # 나중에 들어온 원소부터 출력