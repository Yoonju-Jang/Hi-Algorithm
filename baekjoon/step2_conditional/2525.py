#2525
A, B = map(int,input().split())
C = int(input())
total =  A * 60 + B + C
if total >= 60*24:
    total -= 60*24
H = total // 60
M = total % 60
print(H, M)