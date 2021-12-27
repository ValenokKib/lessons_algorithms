import collections

enterprise = collections.namedtuple('enterprise',  ['name', 'q1', 'q2', 'q3', 'q4', 'sum_q'])
enterprises = []
n = int(input('Количество предприятий: '))
total_e = 0 #счетчик прибыли по предприятиям
for i in range(n):
    name = input(f'Название {i + 1} предприятия: ')
    q1 = int(input('Прибыль за 1-й квартал: ')) #1 квартал
    q2 = int(input('Прибыль за 2-й квартал: ')) #2 квартал
    q3 = int(input('Прибыль за 3-й квартал: ')) #3 квартал
    q4 = int(input('Прибыль за 4-й квартал: ')) #4 квартал
    sum_q = q1 + q2 + q3 + q4 #общая прибыль предприятия за год
    enterprises.append(
        enterprise(name=name, q1=q1, q2=q2, q3=q3, q4=q4, sum_q=sum_q)
    )
    total_e += sum_q #суммируем прибыль предприятий
#print(enterprises)

total_sum_q = total_e / n
print(f'Средняя прибыль предприятий: {total_sum_q}')
for enterprise in enterprises:
    if enterprise.sum_q >= total_sum_q:
        print(f'Предприятие {enterprise.name} имеет прибыль выше средней')
    else:
        print(f'Предприятие {enterprise.name} имеет прибыль ниже средней')