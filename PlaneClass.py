from CircleClass import Circle
from WideAngleClass import WideAngle, create_equation, check_pos

from collections import deque
from math import sqrt, pi, acos, sin


class Plane:
    def __init__(self, center_x, center_y, scale=1):
        self.scale = round(scale)
        self.dots = deque()
        self.circles = list()
        self.angles = list()
        self.my_circle = None
        self.my_angle = None
        self.center = (center_x, center_y)
        # self.circles.append(Circle(70, 40, 100, -40))
        # self.angles.append(WideAngle(1, 1, 20, 20, 10, 10))

    def clear(self):
        self.circles.clear()
        self.angles.clear()
        self.my_circle = None
        self.my_angle = None

    def add(self, obj):
        try:
            if obj.type == "Circle":
                self.circles.append(obj)
            elif obj.type == "Angle":
                self.angles.append(obj)
        except:
            self.dots.append(obj)

    def addFromFile(self, fname):
        txt = open(fname, mode="r")
        str = txt.readlines()
        for s in str:
            points = extractNumbers(s)
            if len(points) == 4:
                self.circles.append(Circle(points[0], points[1], points[2], points[3]))
            else:
                self.angles.append(
                    WideAngle(points[0], points[1], points[2], points[3], points[4], points[5]))
        txt.close()

    def calculateCross(self):
        max_area = 0
        for angle in self.angles:
            for circle in self.circles:
                area, r = 0, circle.radius
                firstPoints, mainPoints, secondPoints, inAngle = findCrossPoints(angle, circle)
                countOfPoints = len(firstPoints) + len(mainPoints) + len(secondPoints)
                x1, y1, x2, y2 = angle.mainSegment[0], angle.mainSegment[1], \
                                 angle.mainSegment[2], angle.mainSegment[3]
                # x0, y0 = circle.center[0], circle.center[1]
                if countOfPoints < 2:
                    area = pi * (r ** 2) if inAngle else 0
                elif countOfPoints < 4:
                    if len(firstPoints) == 1 and len(secondPoints) == 1:
                        # случай с прямоугольной трапецией
                        x4, y4, x5, y5 = firstPoints[0][0], firstPoints[0][1], secondPoints[0][0], \
                                         secondPoints[0][1]
                        h = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # высота трапеции
                        # стороны трапеции
                        a = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
                        b = sqrt((x2 - x5) ** 2 + (y2 - y5) ** 2)
                        area += h * (a + b) / 2  # площадь трапеции
                        # ищем площадь сегмента
                        area += RoundSegmentArea(x4, y4, x5, y4, r)
                    elif len(mainPoints) == 1:
                        Points = list()
                        if len(firstPoints) == 1:
                            Points = firstPoints if firstPoints != mainPoints else Points
                        if len(secondPoints) == 1:
                            Points = secondPoints if secondPoints != mainPoints else Points
                        x4, y4, x5, y5 = mainPoints[0][0], mainPoints[0][1], Points[0][0], \
                                         Points[0][1]
                        # x, y = точка, которая лежит внутри окружности
                        '''if angle.vertical:
                            if min(y4, y5) <= y1 <= max(y4, y5):
                                x, y = x1, y1
                            if min(y4, y5) <= y2 <= max(y4, y5):
                                x, y = x2, y2
                        else:
                            if min(x4, x5) <= x1 <= max(x4, x5):
                                x, y = x1, y1
                            if min(x4, x5) <= x2 <= max(x4, x5):
                                x, y = x2, y2'''
                        x, y = x1, y1
                        a = sqrt((x - x4) ** 2 + (y - y4) ** 2)
                        b = sqrt((x - x5) ** 2 + (y - y5) ** 2)
                        area += a * b / 2
                        area += RoundSegmentArea(x4, y4, x5, y4, r)
                    else:
                        if len(firstPoints) == 2:
                            Points = firstPoints
                        elif len(secondPoints) == 2:
                            Points = secondPoints
                        else:
                            Points = mainPoints
                        x4, y4, x5, y5 = Points[0][0], Points[0][1], Points[1][0], Points[1][1]
                        area += RoundSegmentArea(x4, y4, x5, y4, r)
                        if inAngle:
                            area = pi * (r ** 2) - area
                elif countOfPoints < 6:
                    if len(firstPoints) == 2 and len(secondPoints) == 2:
                        area = pi * r ** 2
                        area -= RoundSegmentArea(firstPoints[0][0], firstPoints[0][1],
                                                 firstPoints[1][0], firstPoints[1][1], r)
                        area -= RoundSegmentArea(secondPoints[0][0], secondPoints[0][1],
                                                 secondPoints[1][0], secondPoints[1][0], r)
                    if len(mainPoints) == 2:
                        if len(firstPoints) == 2:
                            Points = firstPoints
                        elif len(secondPoints) == 2:
                            Points = secondPoints
                        area = pi * r ** 2
                        area -= RoundSegmentArea(Points[0][0], Points[0][1],
                                                 Points[1][0], Points[1][1], r)
                        area -= RoundSegmentArea(mainPoints[0][0], mainPoints[0][1],
                                                 mainPoints[1][0], mainPoints[1][1], r)
                    else:
                        if len(secondPoints) == 2:
                            firstPoints, secondPoints = secondPoints, firstPoints
                            x1, y1, x2, y2 = x2, y2, x1, y1
                        x4, y4 = mainPoints[0][0], mainPoints[0][1]
                        x7, y7 = secondPoints[0][0], secondPoints[0][1]
                        x5, y5, x6, y6 = firstPoints[0][0], firstPoints[0][1], firstPoints[1][0], \
                                         firstPoints[1][1]
                        AB = sqrt((x1 - x5) ** 2 + (y1 - y5) ** 2)
                        CB = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
                        b = sqrt((x1 - x6) ** 2 + (y1 - y6) ** 2)
                        if AB > b:
                            AB, b = b, AB
                            x5, y5, x6, y6 = x6, y6, x5, y5
                        a = sqrt((x2 - x7) ** 2 + (y2 - y7) ** 2)
                        h = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        area += h * (a + b) / 2
                        area -= AB * CB / 2
                        area += RoundSegmentArea(x4, y4, x5, y5, r)
                else:
                    area = pi * r ** 2
                    area -= RoundSegmentArea(mainPoints[0][0], mainPoints[0][1], mainPoints[1][0],
                                             mainPoints[1][1])
                    area -= RoundSegmentArea(firstPoints[0][0], firstPoints[0][1],
                                             firstPoints[1][0], firstPoints[1][1])
                    area -= RoundSegmentArea(secondPoints[0][0], secondPoints[0][1],
                                             secondPoints[1][0], secondPoints[1][1])
                if area > max_area:
                    max_area = area
                    self.my_circle = circle
                    self.my_angle = angle
        return round(max_area / 100, 2)


def findCrossPoints(angle, circle):
    if angle.vertical:
        pass
    if angle.horizontal:
        pass
    else:
        x1, y1, x2, y2 = angle.mainSegment[0], angle.mainSegment[1], angle.mainSegment[
            2], angle.mainSegment[3]
        x4, y4, x5, y5 = angle.firstSegment[2], angle.firstSegment[3], \
                         angle.secondSegment[2], angle.secondSegment[3]
        x0, y0, r = circle.center[0], circle.center[1], circle.radius
        m_k, m_b = create_equation(x1, y1, x2, y2)
        k1, b1 = create_equation(x1, y1, x4, y4)
        k2, b2 = create_equation(x2, y2, x5, y5)
        inAngle = False
        if check_pos(x1, y1, x2, y2, x0, y0) == angle.pos and check_pos(
                x1, y1, x4, y4, x0, y0) != check_pos(x2, y2, x5, y5, x0, y0):
            inAngle = True
        # Точки пересечения окружности с главным сегментом
        mainPoints = list()
        D4 = (m_k ** 2) * (m_b ** 2) - (1 + m_k ** 2) * (m_b ** 2 - r ** 2)
        if D4 >= 0:
            x = (-m_k * m_b + sqrt(D4)) / (1 + m_k ** 2)
            xo = (-m_k * m_b - sqrt(D4)) / (1 + m_k ** 2)
            if min(x1, x2) < x < max(x1, x2):
                y = m_k * x + m_b
                mainPoints.append((x, y))
            if min(x1, x2) < xo < max(x1, x2):
                y = m_k * xo + m_b
                mainPoints.append((xo, y))
        # Точки пересечения с "первым" сегментом
        firstPoints = list()
        D4 = (k1 ** 2) * (b1 ** 2) - (1 + k1 ** 2) * (b1 ** 2 - r ** 2)
        if D4 >= 0:
            x = (-k1 * b1 + sqrt(D4)) / (1 + k1 ** 2)
            xo = (-k1 * b1 - sqrt(D4)) / (1 + k1 ** 2)
            if min(x1, x4) < x < max(x1, x4):
                y = k1 * x + b1
                firstPoints.append((x, y))
            if min(x1, x4) < xo < max(x1, x4):
                y = k1 * xo + b1
                firstPoints.append((xo, y))
        secondPoints = list()
        D4 = (k2 ** 2) * (b2 ** 2) - (1 + k2 ** 2) * (b2 ** 2 - r ** 2)
        if D4 >= 0:
            x = (-k2 * b2 + sqrt(D4)) / (1 + k2 ** 2)
            xo = (-k2 * b2 - sqrt(D4)) / (1 + k2 ** 2)
            if min(x5, x2) < x < max(x5, x2):
                y = k2 * x + b2
                secondPoints.append((x, y))
            if min(x5, x2) < xo < max(x5, x2):
                y = k2 * xo + b2
                secondPoints.append((xo, y))
    return firstPoints, mainPoints, secondPoints, inAngle


def extractNumbers(string):
    points = list()
    x = ""
    for i in range(len(string)):
        if string[i].isdigit():
            x += string[i]
        elif x != "":
            points.append(int(x))
            x = ""
    if x != "":
        points.append(int(x))
    return points


def RoundSegmentArea(x1, y1, x2, y2, r):
    l = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    a = acos((2 * r ** 2 - l ** 2) / (2 * r ** 2))
    area = ((r ** 2) / 2) * (a - sin(a))
    return area
