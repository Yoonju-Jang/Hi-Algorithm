#8958(구글 도움받음)

n = int(input())
for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

# 배울점: score/sum_score 구분해 설정

# Best
import sys
n = int(input())
s = 0
for _ in range(n):
    l = sys.stdin.readline().rstrip().split('X')
    for i in range(len(l)):
        s += sum(range(len(l[i])+1))
    print(s)
    s=0

# 배울점: 1)score에 영향을 주지 않는 X는 삭제
#         2) 1+2+3 이 순서에서 range를 떠올리는 센스
