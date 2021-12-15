

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 74, -15, -7, 23, 43, 7, 7, 7, 34, 89]

min_index = 0
max_index = 0
sum = 0

for i in range(len(arr)):
    if arr[i] < arr[min_index]:
        min_index = i
    elif arr[i] > arr[min_index]:
        max_index = i

for i in range(min_index, max_index):
    sum += arr[i]

print(f'Минимальный элемент массива {arr[min_index]};\nМаксимальный элемент массива {arr[max_index]}')
print(f'Сумма элементов от минимума до максимума равно: {sum}')
