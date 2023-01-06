# 3) 문자열 재정렬
import re

s = input()
alphas = re.findall('[a-zA-Z]', s)
numbers = re.findall('\d', s)

s1 = ''.join(sorted(alphas))
s2 = sum(list(map(int,numbers)))
#s2 = sum([int(i) for i in numbers])
print(s1+str(s2))

# 배울점
# 1. 정규표현식의 강력함
# 2. 문자열 정렬
# 3. 리스트 숫자-> 문자 변환

## 답안 비교
data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트 삽입
    if x.isalpha():    # isalpha 이외에 isdigit, isnumeric 존재
        result.append(x)
    # 숫자는 따로 더하기
    else:                
        value += int(x)

#알파벳 오름차순 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))