# 1) 시각
# 00시00분00초-N시59분59초
# 3이 하나라도 포함되는 모든 경우의 수

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # '3'이 포함된 경우
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)