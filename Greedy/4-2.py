import time
start_time = time.time()

N = int(input())

X = 1
Y = 1

answer = input().split()

for i in answer:
    if i =='L':
        X -=1
        if X <1:
            X =1
    elif i == 'R':
        X +=1
        if X >N:
            X=N

    elif i == 'U':
        Y -=1
        if Y<1:
            Y =1
    elif i == 'D':
        Y += 1
        if Y>N:
            Y =N

print(Y,end=" ")
print(X)


end_time = time.time()
print("time : ", end_time-start_time)#수행시간 출력


"""

n = int(input())

x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    # 이동 수행
    x, y = nx, ny

print(x, y)


"""
