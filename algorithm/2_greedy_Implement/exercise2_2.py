# 2) 왕실의 나이트

# 현재 나이트 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
#int(ord(input_data[0])) - 96ㄴ
# ord(문자): 유니코드 정수 반환 <-> chr(정수): 해당 문자 반환

# 나이트가 이동할 수 있는 8가지 방향 정의
# !! dx, dy 말고 이렇게도 사용 가능 !!
steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지
result=0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능한가 <=> 체스판을 벗어나지 않는가
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <=8:
        result += 1

print(result)