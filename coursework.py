'''
----------------------------------------------------------------------
    Программа coursework
    Курсовой проект
    по предмету "Технология разработки программного обеспечения".
    Язык: Python
    Разработал: Волков Н.Е.
----------------------------------------------------------------------
    Задание:
    Разработка программы вычисления определителя высшего порядка
    путём разложения по строке(столбцу).
----------------------------------------------------------------------
    Функции и методы:
    __init__ - метод, являющийся инициализатором, предназначенным для
    создания инстансов.
    inputSize - функция для ввода размера матрицы пользователем.
    checkSize - функция, проверяющая размер матрицы на условное ограничение.
    outputSizeWarnin - функция, выводящая сообщение об ошибке ввода размера.
    matrixFill - функция для заполнения матрицы пользователем.
    outputOrders - функция, выполняющая роль интерфейса для вызова
    функций вывода определителей.
    outputSecondOrder - функция для вывода определителя второго порядка.
    outputThirdOrder - функция для вывода определителя третьего порядка.
    outputFourthOrder - функция для вывода определителя четвертого порядка.
    outputFifthOrder - функция для вывода определителя пятого порядка.
    secondOrder - функция, вычисляющая определитель второго порядка.
    thirdOrder - функция, вычисляющая определитель третьего порядка.
    fourthOrder - функция, вычисляющая определитель четвертого порядка.
    fifthOrder - функция, вычисляющая определитель пятого порядка.
    Матрицы:
    matrix - вводимая матрица.
    first_minor - первый минор матрицы matrix.
    second_minor - второй минор матрицы matrix.
    third_minor - третий минор матрицы matrix.
    fourth_minor - четвёртый минор матрицы matrix.
    fifth_minor - пятый минор матрицы matrix.
    Переменные:
    i - счётчик строк.
    j - счётчик столбцов.
    size - количество строк и столбцов в матрице.
'''


class Determinant(object):

    '''
        Метод-инициализатор, является встроенным методом языка
        python. Необходим для объявления констант и вызова
        управляющих функций и методов.
        Глобальные переменные:
        matrix - вводимая матрица.
        first_minor - первый минор матрицы matrix.
        second_minor - второй минор матрицы matrix.
        third_minor - третий минор матрицы matrix.
        fourth_minor - четвёртый минор матрицы matrix.
        fifth_minor - пятый минор матрицы matrix.
        size - размер матрицы.
        Локальные переменные:
        size - экземпляр глобальной переменной size.
    '''

    def __init__(self):
        self.inputSize()
        size = self.size
        self.matrix = [[0] * size for i in range(size)]
        self.matrixFill()
        self.first_minor = [[0] * size for i in range(size)]
        self.second_minor = [[0] * size for i in range(size)]
        self.third_minor = [[0] * size for i in range(size)]
        self.fourth_minor = [[0] * size for i in range(size)]
        self.fifth_minor = [[0] * size for i in range(size)]
        self.outputOrders()

    '''
        Функция для ввода размера матрицы пользователем.
        Глобальные переменные:
        size - размер матрицы.
    '''

    def inputSize(self):
        print('Введите размер квадратной матрицы: ')
        self.size = int(input())
        self.checkSize()

    '''
        Функция, проверяющая размеры матрицы на условное ограничение.
        Глобальные параметры:
        size - размер матрицы.
        Локальные переменные:
        size - экземпляр глобальной переменной size.
    '''

    def checkSize(self):
        size = self.size
        if (size > 5 ) or (size < 2):
            self.outputSizeWarning()
            self.inputSize()
        else:
            return 0

    '''
        Функция, выводящая сообщение об ошибке ввода размера.
    '''

    def outputSizeWarning(self):
        print('От 2 до 5 включительно!')

    '''
        Функция для заполнения матрицы пользователем.
        Глобальные переменные:
        matrix - вводимая матрица.
        size - размер матрицы.
        Локальные переменные:
        matrix - экземпляр глобальной переменной matrix.
        size - экземпляр глобальной переменной size.
        i - счётчик строк.
        j - счётчик столбцов.
    '''

    def matrixFill(self):
        matrix = self.matrix
        size = self.size
        print('Введите матрицу в горизонтальном порядке:')
        for i in range(size):
            for j in range(size):
                matrix[i][j] = float(input())

    '''
        Функция, выполняющая роль интерфейса для вызова функций вывода
        определителей.
        Глобальные переменные:
        size - размер матрицы.
        Локальные переменные:
        size - экземпляр глобальной переменной size.
    '''

    def outputOrders(self):
        size = self.size
        if size == 2:
            self.outputSecondOrder()
        elif size == 3:
            self.outputThirdOrder()
        elif size == 4:
            self.outputFourthOrder()
        elif size == 5:
            self.outputFifthOrder()

    '''
        Функция для вывода определителя второго порядка.
        Глобальные переменные:
        matrix - вводимая матрица.
    '''

    def outputSecondOrder(self):
        print(self.secondOrder(self.matrix))

    '''
        Функция для вывода определителя третьего порядка.
        Глобальные переменные:
        matrix - вводимая матрица.
    '''

    def outputThirdOrder(self):
        print(self.thirdOrder(self.matrix))

    '''
        Функция для вывода определителя четвёртого порядка.
        Глобальные переменные:
        matrix - вводимая матрица.
    '''

    def outputFourthOrder(self):
        print(self.fourthOrder(self.matrix))

    '''
        Функция для вывода определителя пятого порядка.
        Глобальные переменные:
        matrix - вводимая матрица.
    '''

    def outputFifthOrder(self):
        print(self.fifthOrder(self.matrix))

    '''
        Функция, вычисляющая определитель второго порядка.
        Локальные переменные:
        matrix - передаваемый функции аргумент, являющийся вводимой матрицой.
    '''

    def secondOrder(self, matrix):
        second_order = matrix[0][0] * matrix[1][1] - \
            matrix[0][1] * matrix[1][0]
        return second_order

    '''
        Функция, вычисляющая определитель третьего порядка.
        Локальные переменные:
        matrix - передаваемый функции аргумент, являющийся вводимой матрицой.
    '''

    def thirdOrder(self, matrix):
        first_minor = self.first_minor
        second_minor = self.second_minor
        third_minor = self.third_minor
        for i in range(2):
            for j in range(2):
                first_minor[i][j] = matrix[i+1][j+1]
                third_minor[i][j] = matrix[i+1][j]
        second_minor[0][0] = matrix[1][0]
        second_minor[0][1] = matrix[1][2]
        second_minor[1][0] = matrix[2][0]
        second_minor[1][1] = matrix[2][2]
        third_order = matrix[0][0] * self.secondOrder(first_minor) - \
            matrix[0][1] * self.secondOrder(second_minor) + \
            matrix[0][2] * self.secondOrder(third_minor)
        return third_order

    '''
        Функция, вычисляющая определитель четвёртого порядка.
        Локальные переменные:
        matrix - передаваемый функции аргумент, являющийся вводимой матрицой.
    '''

    def fourthOrder(self, matrix):
        first_minor = self.first_minor
        second_minor = self.second_minor
        third_minor = self.third_minor
        fourth_minor = self.fourth_minor
        for i in range(3):
            for j in range(3):
                first_minor[i][j] = matrix[i+1][j+1]
                fourth_minor[i][j] = matrix[i+1][j]
        second_minor[0][0] = matrix[1][0]
        second_minor[1][0] = matrix[2][0]
        second_minor[2][0] = matrix[3][0]
        second_minor[0][1] = matrix[1][2]
        second_minor[1][1] = matrix[2][2]
        second_minor[2][1] = matrix[3][2]
        second_minor[0][2] = matrix[1][3]
        second_minor[1][2] = matrix[2][3]
        second_minor[2][2] = matrix[3][3]
        third_minor[0][0] = matrix[1][0]
        third_minor[1][0] = matrix[2][0]
        third_minor[2][0] = matrix[3][0]
        third_minor[0][1] = matrix[1][2]
        third_minor[1][1] = matrix[2][2]
        third_minor[2][1] = matrix[3][2]
        third_minor[0][2] = matrix[1][3]
        third_minor[1][2] = matrix[2][3]
        third_minor[2][2] = matrix[3][3]
        fourth_order = matrix[0][0] * self.thirdOrder(first_minor) - \
            matrix[0][1] * self.thirdOrder(second_minor) + \
            matrix[0][2] * self.thirdOrder(third_minor) - \
            matrix[0][3] * self.thirdOrder(fourth_minor)
        return fourth_order

    '''
        Функция, вычисляющая определитель пятого порядка.
        Локальные переменные:
        matrix - передаваемый функции аргумент, являющийся вводимой матрицой.
    '''

    def fifthOrder(self, matrix):
        first_minor = self.first_minor
        second_minor = self.second_minor
        third_minor = self.third_minor
        fourth_minor = self.fourth_minor
        fifth_minor = self.fifth_minor
        for i in range(4):
            for j in range(4):
                first_minor[i][j] = matrix[i+1][j+1]
                fifth_minor[i][j] = matrix[i+1][j]
        second_minor[0][0] = matrix[1][0]
        second_minor[1][0] = matrix[2][0]
        second_minor[2][0] = matrix[3][0]
        second_minor[3][0] = matrix[4][0]
        second_minor[0][1] = matrix[1][2]
        second_minor[1][1] = matrix[2][2]
        second_minor[2][1] = matrix[3][2]
        second_minor[3][1] = matrix[4][2]
        second_minor[0][2] = matrix[1][3]
        second_minor[1][2] = matrix[2][3]
        second_minor[2][2] = matrix[3][3]
        second_minor[3][2] = matrix[4][3]
        second_minor[0][3] = matrix[1][4]
        second_minor[1][3] = matrix[2][4]
        second_minor[2][3] = matrix[3][4]
        second_minor[3][3] = matrix[4][4]
        third_minor[0][0] = matrix[1][0]
        third_minor[1][0] = matrix[2][0]
        third_minor[2][0] = matrix[3][0]
        third_minor[3][0] = matrix[4][0]
        third_minor[0][1] = matrix[1][2]
        third_minor[1][1] = matrix[2][2]
        third_minor[2][1] = matrix[3][2]
        third_minor[3][1] = matrix[4][2]
        third_minor[0][2] = matrix[1][3]
        third_minor[1][2] = matrix[2][3]
        third_minor[2][2] = matrix[3][3]
        third_minor[3][2] = matrix[4][3]
        third_minor[0][3] = matrix[1][4]
        third_minor[1][3] = matrix[2][4]
        third_minor[2][3] = matrix[3][4]
        third_minor[3][3] = matrix[4][4]
        fourth_minor[0][0] = matrix[1][0]
        fourth_minor[1][0] = matrix[2][0]
        fourth_minor[2][0] = matrix[3][0]
        fourth_minor[3][0] = matrix[4][0]
        fourth_minor[0][1] = matrix[1][2]
        fourth_minor[1][1] = matrix[2][2]
        fourth_minor[2][1] = matrix[3][2]
        fourth_minor[3][1] = matrix[4][2]
        fourth_minor[0][2] = matrix[1][3]
        fourth_minor[1][2] = matrix[2][3]
        fourth_minor[2][2] = matrix[3][3]
        fourth_minor[3][2] = matrix[4][3]
        fourth_minor[0][3] = matrix[1][4]
        fourth_minor[1][3] = matrix[2][4]
        fourth_minor[2][3] = matrix[3][4]
        fourth_minor[3][3] = matrix[4][4]
        fifth_order = matrix[0][0] * self.fourthOrder(first_minor) - \
            matrix[0][1] * self.fourthOrder(second_minor) + \
            matrix[0][2] * self.fourthOrder(third_minor) - \
            matrix[0][3] * self.fourthOrder(fourth_minor) + \
            matrix[0][4] * self.fourthOrder(fifth_minor)
        return fifth_order

determinant = Determinant()
