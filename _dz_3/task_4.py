

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 74, -15, -7, 23, 43, 7, 7, 7, 34, 89]

many_num = 0 # индекс элемента массива встречающегося чаще всего    44444444

for i in range(len(arr)):
    if arr.count(many_num) < arr.count(i):
        many_num = arr.index(i)

print(f'В массиве число: {arr[many_num]}, встречается {arr.count(arr[many_num])} раз')