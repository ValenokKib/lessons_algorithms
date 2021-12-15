
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 74, -15, -7, 23, 43, 7, 7, 7, 34, 89]
arr_even = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr_even.append(i)

print(arr)
print(f'Индексы четных элементов массива arr: {arr_even}')