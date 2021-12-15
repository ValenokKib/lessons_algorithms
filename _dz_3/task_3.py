
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
