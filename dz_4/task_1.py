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
# def multiplicity_1():
#     arr = [0] * 8   #создаем пустой массив ячеек кратным диапозову от 2 до 9
#     for i in range(2, 1000000):  #прогоняем в цикле массив от 2 до 99
#         for j in range(2, 10):  #проверяем кратность внешнего значения диапозона внутреннему
#             if i % j == 0:
#                 arr[j - 2] += 1  #если значение внешнего диапозона кратно значению внутреннего - увеличиваем счетчитк на 1
#
#     for n in range(len(arr)):  #прогоняем полученный массив по длине для вывода кол-ва кратных элементов
#         print(f'На {n + 2} делится {arr[n]} элементов массива')
#
# multiplicity_1()
#O(1)  время исполнения =  0.45302367210388184

#
@time_of_func
def multiplicity():
    arr = {}
    for i in range(2, 10):
        arr[i] = []
        for j in range(2, 1000000):
            if j % i == 0:
                arr[i].append(j)
        print(f'Для числа {i} кратны: {len(arr[i])} элементов массива')

multiplicity()

# O(1) время исполнения =  0.370267391204834
