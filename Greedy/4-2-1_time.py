import time
start_time = time.time()

N = int(input())

count = 0

for i in range(N +1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)



end_time = time.time()
print("time : ", end_time-start_time)#수행시간 출력





"""
import time
start_time = time.time()


end_time = time.time()
print("time : ", end_time-start_time)#수행시간 출력

"""
