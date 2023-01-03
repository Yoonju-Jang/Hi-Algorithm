#10871
N, X = map(int, input().split())
sec = list(map(int,input().split()))
for i in sec:
    if i < X:
        print(i, end=' ')
    else: 
        continue

# 모범답안
n, x = map(int, input().split())
a = input().split() # list를 명시하지 않아도 자동 생성

for i in a:
    if int(i) < x:
        print(i, end= " ")
