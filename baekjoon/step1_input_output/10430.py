#10430
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

# 강력한 sep의 역할!! 
# end는 문장 끝, sep는 구분자.