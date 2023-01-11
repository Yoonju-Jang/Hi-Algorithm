#2577
a = int(input())
b = int(input())
c = int(input())

s = str(a * b * c)
cnt = []
for i in range(10):
    cnt.append(s.count(str(i)))
for i in cnt: print(i) 