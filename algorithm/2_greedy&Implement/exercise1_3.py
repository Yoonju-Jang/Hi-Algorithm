# 3) 모험가 길드
# 공포도=x -> x명 이상 그룹에만 참여 가능
# 결론: 여행을 떠날 수 있는 최대 그룹 수

n = int(input()) 
fear = list(map(int,input().split()))
fear.sort()

num = 0    # 현재 그룹에 포함된 모험가 수
group = 0   # 총 그룹 수
for i in fear:
      num+=1
      if num >= i:
        num=0     # 현재 그룹에 포함된 모험가 수 초기화
        group+=1
print(group)