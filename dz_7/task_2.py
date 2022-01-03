import random

def merge_sort(array_to_sort):
    a = array_to_sort
    if len(a) <= 1:
        return a
    mid_arr = len(a) // 2
    l_arr = merge_sort(a[:mid_arr])
    r_arr = merge_sort(a[mid_arr:])
    return merge(l_arr, r_arr, a.copy())

def merge(l_arr, r_arr, merged):
    i = 0
    j = 0
    while i < len(l_arr) and j < len(r_arr):
       if l_arr[i] <= r_arr[j]:
           merged[i + j] = l_arr[i]
           i += 1
       else:
           merged[i + j] = r_arr[j]
           j += 1
    for i in range(i, len(l_arr)):
        merged[i + j] = l_arr[i]
    for j in range(j, len(r_arr)):
        merged[i + j] = r_arr[j]

    return merged

arr = [random.uniform(0, 50) for i in range(10)]

print(f'Исходный массив случайных чисел:\n{arr}')
print(f'Сортировка массива по убыванию:\n{merge_sort(arr)}')

