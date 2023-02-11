# 1로 만들기
x = int(input())

# DP 테이블 초기화
d = [0] * 30001

# 보텀업, d[i] 비교를 통해 계속 갱신
# 왜 2일때부터? d[1]은 어차피 0
for i in range(2,x+1):
    d[i] = d[i-1]+1
    if i % 2 == 0 :
        d[i] = min(d[i],d[i//2]+1)
    if i % 3 == 0 :
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0 :
        d[i] = min(d[i],d[i//5]+1)

print(d[x])
    
