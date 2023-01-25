# 1181번: 단어 정렬
from sys import stdin
n = int(input())

str = []
for _ in range(n):
    str.append(stdin.readline().rstrip())

str = list(set(str))
str.sort(key = lambda x:(len(x),x))
for s in str: print(s)