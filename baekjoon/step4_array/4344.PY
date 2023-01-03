#4344
C = int(input())
for _ in range(C):
    l = list(map(int,input().split()))
    avg = sum(l[1:])/l[0]
    cnt = 0
    for i in l[1:]:
        if i > avg:
            cnt +=1
    over_avg = cnt/l[0]*100
    print(f'{over_avg:.3f}%')

# 1) 일렬로 입력받을땐 -> 리스트[:] 잘 활용하기
# 2) if 구문에서 꼭 else 안써도 됨
# 3) f-string 소수점 자릿수 지정하는 법