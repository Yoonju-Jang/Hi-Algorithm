#2577: 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

s = str(a * b * c)
cnt = []
for i in range(10):
    cnt.append(s.count(str(i)))
for i in cnt: print(i) 


# 주희 풀이 
digit_list = [0] * 10  # 오!! 다음에 써먹자.

a = int(input())
b = int(input())
c = int(input())
products = a * b * c

for char in str(products):
    digit_list[int(char)] += 1

for digit in digit_list:
    print(digit)