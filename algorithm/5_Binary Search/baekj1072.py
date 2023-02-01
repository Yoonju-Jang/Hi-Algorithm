# 1072번: 게임
import sys
input = sys.stdin.readline

x, y = map(int,input().split())

z = (y*100)//x
#round(y/x,2)*100
if z >= 99:
    print(-1)
else:
    answer = 0  # 몇 판 더하는가
    start = 1
    end = x

    while(start <= end):
        mid = (start+end)//2
        # Z 변화x (오른쪽 탐색)
        if (y+mid)*100 // (x+mid) <= z:
            start = mid+1
        # Z 변화0 (왼쪽 탐색)
        else:
            answer = mid  
            end = mid-1

    print(answer)