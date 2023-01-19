#1157: 단어공부
s = input().upper()
s1 = ''.join(sorted(s)) 
# 대문자 변환과 정렬을 마친 string
s_ele = sorted(set(s))
# string에 사용된 alphabet

cnt = [] #string에 사용된 alphabet별 갯수
for i in s_ele:
    cnt.append(s1.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(s_ele[cnt.index(max(cnt))])



# 주희 풀이: '구현' 방법에 적합!!
str = input()
str = str.upper()
letter_count = -1

#for문 구조 잘 익히기!!
for letter in set(str):
    if letter_count == str.count(letter):
        output = '?'
    elif letter_count < str.count(letter):
        output = letter
        letter_count = str.count(letter)

print(output)


