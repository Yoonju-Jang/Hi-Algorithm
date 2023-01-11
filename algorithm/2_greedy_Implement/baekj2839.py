#2839: 설탕배달

N = int(input())
cnt_5 = N//5 # 5kg 최대 봉지수

for i in range(cnt_5,-1,-1):
    left = N-(5*i)
    if left%3 == 0 or left == 0:
        cnt_5 = i
        if left == 0:
            print(int(cnt_5))
            break
        else: 
            cnt_3 = left/3
            print(int(cnt_5 + cnt_3))
            break
    elif i == 0: 
        print(-1)

# 주희 풀이(깔끔하다..)-> left==0을 고려할 필요가 없었음
while a >= 0:
    gap = n - a * 5
    if gap % 3 == 0:  
        print(a + gap//3)
        exit()
    else:
        a -= 1

print(-1)
exit()

# 얻어갈 점
# 1) def로 정의한 함수 내의 변수만 local변수
# 2) break 대신 exit() 사용가능