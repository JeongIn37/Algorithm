# 거스름돈

n = int(input())
cnt = 0

coins = [500, 100, 50, 10]
for coin in coins:
    cnt += n // coin
    n %= coin

print(cnt)