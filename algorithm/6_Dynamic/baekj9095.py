# 9095번: 1, 2, 3 더하기

t = int(input())
for _ in range(t):
    n = int(input())

    # dp 테이블
    d = [0] * 11
    d[1] = 1
    d[2] = 2
    d[3] = 4

    if n in (1,2,3): print(d[n])
    else: 
        # 보텀업
        for i in range(4, n + 1):
            for k in (1,2,3):
                if i - k >= 1:
                    d[i] += d[i - k]

        print(d[n])