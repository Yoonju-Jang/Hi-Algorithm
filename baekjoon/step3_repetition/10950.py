#10950
SUM = []
N = int(input())
for i in range(N):
    A, B = map(int,input().split())
    SUM.append(A+B)
for i in SUM:
    print(i)