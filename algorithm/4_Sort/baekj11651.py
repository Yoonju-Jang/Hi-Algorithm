# 11651번: 좌표 정렬하기2
from sys import stdin
n = int(input())

dot = []
for _ in range(n):
    dot.append(tuple(map(int,stdin.readline().split())))

dot.sort(key = lambda x:(x[1], x[0]))
for d in dot: print(d[0],d[1])