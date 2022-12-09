import math

def input_num(
    msg: str, 
    min: int = None, 
    max: int = None,
    type_num: type = int,
) -> int:
    '''
    Берет на ввод у пользователя число с дальнейшей проверкой.

    Параметры:
    msg - Сообщение подающееся на ввод пользователю.
    min - Минимальное значение на ввод.
    max - Максимальное значение на ввод.

    Возврат:
    Корректно введенное число.
    '''
    while True:
        try:
            num = type_num(input(msg))
            if min != None and num < min or max != None and num > max:
                min_msg = '' if min == None else f' от {min}'
                max_msg = '' if max == None else f' до {max}'
                print(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                continue
            return num
        except:
            print(f'Ошибка: нужно ввести число типа {type_num}!')

crits = input_num('Введите количество критериев: ', 1)

matrix = []
for i in range(crits):
    row = []
    for j in range(crits):
        if i == j :
            row.append(1)
        else:
            row.append(0)     
    matrix.append(row)



for i in range(crits):
    for j in range(crits):
        if i == j:
            break
        matrix[i][j] = input_num(f'Введите критерий для {i+1} строки и {j+1} столбца: ', type_num=float)
        matrix[j][i] = 1/matrix[i][j]

sum = 0
mults = list()
for i in range(crits):
    mult = 1
    for j in range(crits):
        mult *= matrix[i][j]
    mults.append(math.pow(mult, 1/crits))
    sum += math.pow(mult, 1/crits)

for i in range(crits):
    print(f'Весовой коэффициент для {i+1} критерия:', round(mults[i] / sum, 2))
