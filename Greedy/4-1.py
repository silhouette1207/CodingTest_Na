import time
start_time = time.time()


N, K = map(int,input().split())

answer = 0 
while N !=1:
    if N%K ==0:
        N = N//K
    else:
        N -=1

    answer += 1

print(answer)

end_time = time.time()
print("time : ", end_time-start_time)#수행시간 출력

"""
# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수가 될 때까지 1씩 빼기)
    target = (n // k) * k
    result += (n - target)
    n = target
    
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

"""
