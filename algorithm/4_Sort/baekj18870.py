# 18870번: 좌표 압축
from sys import stdin
n = int(stdin.readline())

dots = list(map(int,stdin.readline().split()))

dots_n = sorted(list(set(dots)))

# .index() -> 시간오류
# for dot in dots:
#     print(dots_n.index(dot),end=' ')

# 딕셔너리 생성
dots_d = dict()
for i in range(len(dots_n)):
    dots_d[dots_n[i]] = i

for dot in dots:
    print(dots_d[dot], end=' ')

# Develope> enumerate 활용-> 시간 단축
from math import inf
data_dict = {x:i for i,x in enumerate(dots_n)}
print(' '.join([str(data_dict[x]) for x in dots]))