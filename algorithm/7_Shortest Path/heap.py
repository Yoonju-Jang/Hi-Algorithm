# min heap - 오름차순 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 우선순위가 낮은 순서대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
    
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# max heap - 내림차순 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 우선순위가 낮은 순서대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
    
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)