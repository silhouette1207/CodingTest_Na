import time
start_time = time.time()

N,M = map(int,input().split())

answer = []
for i in range(N):
    a = list(map(int,input().split()))
    answer.append(a)

num = 0
for i in range(N):
    if min(answer[i]) >num:
        num = min(answer[i])

print(num)



end_time = time.time()
print("time : ", end_time-start_time)#수행시간 출력


"""

n,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))

    min_value = min(data)

    result = max(result,min_value)
print(result)


"""