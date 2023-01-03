#1546
N = int(input())
l = list(map(int,input().split()))

# print(sum(L)/max(L)*100/N) 한 줄로 대체 가능ㅠ
new_grade = [grade/max(l)*100 for grade in l]

sum=0
for i in new_grade:
    sum+=i
print(sum/N)

# 리스트 덧셈은 sum함수 사용하자.
# 파이썬 유용한 내장함수(sum, abs, min/max, round, pow, divmod, eval)