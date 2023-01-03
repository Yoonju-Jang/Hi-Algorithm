#2562
import sys

bin = []
for i in range(9):
    a = int(sys.stdin.readline())
    bin.append(a)

print(max(bin))
print(bin.index(max(bin))+1)
# .index(): 원소의 인덱스 값을 반환

# best
l=[int(input()) for _ in range(9)];x=max(l)
print('%d\n%d' %(x,l.index(x)+1))