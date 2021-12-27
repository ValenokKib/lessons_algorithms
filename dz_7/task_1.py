import random

def bubble_sort(array_to_sort):
    a = array_to_sort
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n += 1
    return a

'''Оптимизация алгоритма сортировки с помощью логического флага'''
# def bubble_sort(array_to_sort):
#     a = array_to_sort
#     n = 1
#     flag = True
#     while flag:
#         flag = False
#         for i in range(len(a) - n):
#             if a[i] < a[i + 1]:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#                 flag = True
#         n += 1
#     return a

array = [random.randint(-100, 100) for i in range(30)]

print(f'Исходный массив случайных чисел:\n{array}')
print(f'Сортировка массива по убыванию:\n{bubble_sort(array)}')