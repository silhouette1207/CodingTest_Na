import time
start_time = time.time()

N, M, K = map(int,input().split())

num = list(map(int,input().split()))

num.sort()

max_num = num[-1]
another_num = num[-2]


if M%K ==0:
    print((M//K-1)*another_num+ (M-M//K)*max_num)
else:
    print((M//K)*another_num + (M-M//K)*max_num)

#time :  3.735650062561035

"""
답지 및 해설
n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m==0:
        break
    result += second
    m-=1
print(result)

#time :  6.548338174819946
"""
end_time = time.time()
print("time : ", end_time-start_time)#수행시간 출력







