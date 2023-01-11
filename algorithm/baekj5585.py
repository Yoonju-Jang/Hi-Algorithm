#5585

n = int(input())
left = 1000 - n  #잔돈
cnt = 0
coins = [500,100,50,10,5,1]
for coin in coins:
    cnt += left//coin
    left %= coin
print(cnt)