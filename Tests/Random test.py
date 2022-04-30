from random import randrange

filename = input("Имя файла:")
count_circle = input("Количество окружностей:")
count_angle = input("Количество \"широких лучей\":")
maxc = input("Максимальный модуль значения координат:")

filename = filename if filename == "" else "test"
filename += ".txt"

try:
    count_circle = 0 if count_circle == "" else int(count_circle)
except:
    count_circle = 0
    print("Количество окружностей - не число")

try:
    count_angle = 0 if count_angle == "" else int(count_angle)
except:
    count_angle = 0
    print("Количество \"широких\" лучей - не число")

try:
    maxc = 300 if maxc == "" else int(maxc)
except:
    maxc = 300
    print("Максимальная координата - не число")

f = open(filename, mode="w")

for i in range(count_circle):
    x, y = randrange(-maxc, maxc), randrange(-maxc, maxc)
    x1 = x
    while x == x1:
        x1 = randrange(-maxc, maxc)
    y1 = y
    while y == y1:
        y1 = randrange(-maxc, maxc)
    f.write(f"{x} {y} {x1} {y1}\n")

for i in range(count_angle):
    x, y = randrange(-maxc, maxc), randrange(-maxc, maxc)
    x1 = x
    while x == x1:
        x1 = randrange(-maxc, maxc)
    y1 = y
    while y == y1:
        y1 = randrange(-maxc, maxc)
    x2 = x
    while x == x2:
        x2 = randrange(-maxc, maxc)
    y2 = y
    while y == y2:
        y2 = randrange(-maxc, maxc)
    f.write(f"{x} {y} {x1} {y1} {x2} {y2}\n")

f.close()
