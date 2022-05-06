steps = [30, 17, 11, 8, 6, 5, 4, 3, 2, 2]  # шаги сетки при разных масштабах


def giveDigit(num, c_x, c_y, rightCorner=False):  # возвращает массив массивов линий
    numbs = list()  # массив цифр
    num = str(num)  # число, которое хотим нарисовать
    n = len(num)  # кол-во цифр в числе
    ind = 0
    if rightCorner:  # если выравнивание по правому краю
        begin, end = c_x - 4 * n + 1, c_x
    else:
        begin, end = c_x - 2 * n + 1, c_x + 2 * n
    for x in range(begin, end, 4):  # перебираем все координаты, в которых должны находиться цифры
        numbs.append(giveNumber(num[ind], x, c_y - 2))  # добавляем массив линий для каждой цифры
        ind += 1
    return numbs


def giveNumber(num, x, y):  # возвращает массив линий для цифры
    if num == "0":
        return giveZero(x, y)
    elif num == "1":
        return giveOne(x, y)
    elif num == "2":
        return giveTwo(x, y)
    elif num == "3":
        return giveThree(x, y)
    elif num == "4":
        return giveFour(x, y)
    elif num == "5":
        return giveFive(x, y)
    elif num == "6":
        return giveSix(x, y)
    elif num == "7":
        return giveSeven(x, y)
    elif num == "8":
        return giveEight(x, y)
    elif num == "9":
        return giveNine(x, y)
    else:
        return giveMinus(x, y)


def giveZero(x0, y0):  # x0, y0 верхний левый угол
    return [[x0, y0, x0, y0 + 5], [x0, y0 + 5, x0 + 2, y0 + 5], [x0 + 2, y0 + 5, x0 + 2, y0],
            [x0 + 2, y0, x0, y0]]


def giveOne(x0, y0):
    return [[x0, y0 + 2, x0 + 2, y0], [x0 + 2, y0, x0 + 2, y0 + 5]]


def giveTwo(x0, y0):
    return [[x0, y0, x0 + 2, y0], [x0 + 2, y0, x0, y0 + 5], [x0, y0 + 5, x0 + 2, y0 + 5]]


def giveThree(x0, y0):
    return [[x0, y0, x0 + 2, y0], [x0 + 2, y0, x0 + 2, y0 + 5], [x0 + 2, y0 + 5, x0, y0 + 5],
            [x0, y0 + 2, x0 + 2, y0 + 2]]


def giveFour(x0, y0):
    return [[x0, y0, x0, y0 + 2], [x0, y0 + 2, x0 + 2, y0 + 2], [x0 + 2, y0, x0 + 2, y0 + 5]]


def giveFive(x0, y0):
    return [[x0 + 2, y0, x0, y0], [x0, y0, x0, y0 + 2], [x0, y0 + 2, x0 + 2, y0 + 2],
            [x0 + 2, y0 + 2, x0 + 2, y0 + 5], [x0 + 2, y0 + 5, x0, y0 + 5]]


def giveSix(x0, y0):
    return [[x0 + 2, y0, x0, y0], [x0, y0, x0, y0 + 5], [x0, y0 + 5, x0 + 2, y0 + 5],
            [x0 + 2, y0 + 5, x0 + 2, y0 + 2], [x0 + 2, y0 + 2, x0, y0 + 2]]


def giveSeven(x0, y0):
    return [[x0, y0, x0 + 2, y0], [x0 + 2, y0, x0, y0 + 5]]


def giveEight(x0, y0):
    return [[x0, y0, x0 + 2, y0], [x0 + 2, y0, x0 + 2, y0 + 5], [x0 + 2, y0 + 5, x0, y0 + 5],
            [x0, y0 + 5, x0, y0], [x0, y0 + 2, x0 + 2, y0 + 2]]


def giveNine(x0, y0):
    return [[x0, y0 + 5, x0 + 2, y0 + 5], [x0 + 2, y0 + 5, x0 + 2, y0], [x0 + 2, y0, x0, y0],
            [x0, y0, x0, y0 + 3], [x0, y0 + 3, x0 + 2, y0 + 3]]


def giveMinus(x0, y0):
    return [[x0, y0 + 2, x0 + 2, y0 + 2]]
