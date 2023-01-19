# 2) 곱하기 혹은 더하기 :100점
# 왼쪽부터 무조건 계산
# x 혹은 + 연산자만 사용가능

s = input()
sum = int(s[0])
for i in range(1,len(s)):
    num = int(s[i])
    if sum<=1 or num<=1:
        sum += num
    else:
        sum *= num
print(sum)
