def recursive_function(i):
    if i == 10:
        return
    print(i,'번째')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료.')

recursive_function(5)