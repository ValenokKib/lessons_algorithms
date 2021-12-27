import random

def median_search(arr, first, last):
    arr = arr.copy()
    mid = len(arr) // 2
    if first >= last:
        return arr[mid]

    pillar = arr[mid]
    i = first
    j = last

    while i <= j:
        while arr[i] < pillar:
            i += 1
        while arr[j] > pillar:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if mid < i:
        arr[mid] = median_search(arr, first, j)
    elif j < mid:
        arr[mid] = median_search(arr, i, last)

    return arr[mid]

m = random.randint(1, 20)
size = 2 * m + 1
array = [random.randint(0, 50) for i in range(size)]
median = median_search(array, 0, len(array) - 1)

print(f'Сгенерирован массив из 2 * {m} + 1 = {size} элементов:\n{array}')
print(f'Медиана: {median}')
