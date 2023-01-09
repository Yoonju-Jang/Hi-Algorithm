#1065
#한수 = 정수 x의 각 자리가 등차수열을 이루면
#1~99:그 갯수만큼 한수 발생
#100>(세자릿수):(첫번째 자리수)-(두번째 자리수)==(두번째 자리수)-(세번째 자리수)

def Hansu(k):
    if k < 100: return k
    else:
        cnt=99
        num_3 = list(map(str,range(100,k+1)))
        for i in num_3:
            if int(i[0])-int(i[1]) == int(i[1])-int(i[2]):
                cnt+=1
        return cnt    

print(Hansu(int(input())))
