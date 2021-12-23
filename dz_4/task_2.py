import time

def time_of_func(func):
    def wrapper():
        start_time = time.time()
        res = func()
        res_time = time.time() - start_time
        print('время исполнения = ', res_time)

        return res

    return wrapper

# @time_of_func
# def numders(): #простой перебор каждого элемента массива
#     a = []
#     n = 500
#     for i in range(2, n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             a.append(i)
#     print(a)
#
# numders()
# O(n) время исполнения при n(500000) =  331.2636241912842
#      время исполнения n(500) =  0.0009725093841552734

@time_of_func
def numbers_1():
    n = 500000
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    k = 2

    while k * k <= n:
        if arr[k] == True:
            d = k * k
            while d <= n:
                arr[d] = False
                d += k
        k += 1

    for i in range(n):
        if arr[i] == True:
            print(i, end=' ')

numbers_1()
# O(n), но алгоритм методом Решета Эратосфена в разы быстрее, время исполнения при n(500000) = 0.20802569389343262

# while True:
#     b = int(input('Введите номер элемента массива простых чисел'))
#     if arr[b] != False:
#         print(f'под i-ым индексом простое число {arr[b]}')
#     else:
#         print('под i-ым индексом число составное, давайте найдем другое')

