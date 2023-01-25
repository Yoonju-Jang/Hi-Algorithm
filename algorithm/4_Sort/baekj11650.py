# 11650번: 좌표 정렬하기
from sys import stdin
n = int(input())

dot = []
for _ in range(n):
    dot.append(tuple(map(int,stdin.readline().split())))

dot.sort(key = lambda x:(x[0], x[1]))
for d in dot: print(d[0],d[1])