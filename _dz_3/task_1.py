

arr = [0] * 8   #создаем пустой массив ячеек кратным диапозову от 2 до 9

for i in range(2, 100):  #прогоняем в цикле массив от 2 до 99
    for j in range(2, 10):  #проверяем кратность внешнего значения диапозона внутреннему
        if i % j == 0:
            arr[j - 2] += 1  #если значение внешнего диапозона кратно значению внутреннего - увеличиваем счетчитк на 1

for n in range(len(arr)):  #прогоняем полученный массив по длине для вывода кол-ва кратных элементов
    print(f'На {n + 2} делится {arr[n]} элементов массива')