import time
start_time = time.time()

N = int(input())
answer = 0
coin_type = [500,100,50,10]

for coin in coin_type:
    answer += N // coin

    N %= coin

print(answer)







end_time = time.time()