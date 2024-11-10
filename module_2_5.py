
def get_matrix(n, m, value): # объявляю функцию get_matrix
    matrix = []
    if n <= 0: # исключаю возможность отрицательных или нулевух значений данных
        return (matrix)
    elif m <= 0:
        return (matrix)
    else:
        print()
    for i in range(n): # пишу первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        matrix.append([])
        for j in range(m): # пишу второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value) # заполняю список значением value
    return (matrix)

result1 = get_matrix(2, 2, 10) # задаю параметр функции
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1) # вывод в консоль
print(result2)
print(result3)














