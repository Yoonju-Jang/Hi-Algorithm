#15552
import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

#여러줄 입력받을 땐 sys.stdin.readline()을 이용한다!