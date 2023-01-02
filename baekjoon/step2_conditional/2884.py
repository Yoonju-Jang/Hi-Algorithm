#2884
H, M = map(int,input().split())
if M >= 45:
    print(H, M-45)
else:
    if H != 0:
        print(H-1, M+15)
    else:
        print(23, M+15)

#모범답안
H, M = map(int,input().split())
total =  H * 60 + M - 45
if total <0:
    total += 60*24
H = total // 60
M = total % 60
print(H, M)

# 배울점) 시간 문제는 분으로 변환해 total로 푸는 것이 유용