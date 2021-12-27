import sys

'''Python 3.9, windows 10 x64'''

# task_1.1
n = int(input('Введите трехзначное число: ')) #  вариант 1

a = n // 100
b = n % 100 // 10
c = n % 10

sum = a + b + c
mult = a * b * c

s_1 = sys.getsizeof(n) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + \
      sys.getsizeof(sum) + sys.getsizeof(mult)
print(s_1)

''' Рез-т
    Введите трехзначное число: 111
    задействовано байт памяти 168'''

n = input('Введите трехзначное число: ') # вариант 2

a = int(n[0])
b = int(n[1])
c = int(n[2])

sum_1 = a + b + c
mult_1 = a * b * c

s_2 = sys.getsizeof(n) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + \
      sys.getsizeof(sum_1) + sys.getsizeof(mult_1)
print(s_2)

''' Рез-т
    Введите трехзначное число: 123
    задействовано байт памяти 192'''

# task_3.3
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 74, -15, -7, 23, 43, 7, 7, 7, 34, 89]
arr_min = 0
arr_max = 0

for i in range(len(arr)):
    if arr[i] < arr[arr_min]:
        arr_min = i
    elif arr[i] > arr[arr_max]:
        arr_max = i
print(f'Массив {arr}\nМинимальный элемент: {arr[arr_min]}\nМаксимальный элемент: {arr[arr_max]}')
a = arr[arr_min]
arr[arr_min] = arr[arr_max]
arr[arr_max] = a
print(f'Минимальный элемент и максимальный в массиве\n{arr} поменяли местами')

s_size = sys.getsizeof(arr) + sys.getsizeof(i) + \
         sys.getsizeof(arr_min) + sys.getsizeof(arr_max) + sys.getsizeof(a)
print(s_size)

''' Рез-т:
    Массив [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 74, -15, -7, 23, 43, 7, 7, 7, 34, 89]
    Минимальный элемент: -45
    Максимальный элемент: 89
    Минимальный элемент и максимальный в массиве
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 89, 74, -15, -7, 23, 43, 7, 7, 7, 34, -45] поменяли местами
    Задействовано байт памяти 360'''